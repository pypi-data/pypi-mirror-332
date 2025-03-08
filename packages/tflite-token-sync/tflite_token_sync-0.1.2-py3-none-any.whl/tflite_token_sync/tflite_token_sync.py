import argparse
from pathlib import Path
import struct
import shutil
from typing import List, Optional

# third_party 디렉토리를 Python 경로에 추가
import sys

sys.path.append("./third_party")

from tflite import Model
import flexbuffers
from platforms.darwinn import Executable, MultiExecutable, Package


# 유틸리티 함수들을 클래스 밖으로 이동
def read_buf(path: Path) -> bytearray:
    """파일에서 바이트 배열을 읽는 함수"""
    with open(path, "rb") as f:
        buf = f.read()
        buf = bytearray(buf)
    return buf


def save_buf(buf: bytearray, path: Path) -> None:
    """바이트 배열을 파일에 저장하는 함수"""
    with open(path, "wb") as f:
        f.write(bytes(buf))


def find_token_pointer(buf: bytearray, token: bytes) -> int:
    """버퍼에서 토큰 포인터를 찾는 함수"""
    pointer = 0
    pointer = buf.find(token, pointer + 1)
    return pointer if pointer != -1 else -1


def change_token(buf: bytearray, pointer: int, new_token: bytes, debug: bool = False) -> None:
    """토큰 값을 변경하는 함수"""
    if debug:
        print("[before change]")
        print(f"pointer: {pointer}, value: {buf[pointer:pointer + 8]}")
    buf[pointer : pointer + 8] = new_token
    if debug:
        print("[after change]")
        print(f"pointer: {pointer}, value: {buf[pointer:pointer + 8]}\n")


def copy_file_to_output_dir(src_path: Path, output_dir: Path) -> Path:
    """파일을 출력 디렉토리로 복사하는 함수"""
    # 출력 디렉토리가 없으면 생성
    output_dir.mkdir(parents=True, exist_ok=True)

    # 대상 파일 경로 생성
    dest_path = output_dir / src_path.name

    # 파일 복사
    shutil.copy2(src_path, dest_path)

    return dest_path


class TfliteTokenSync:
    """TFLite 모델의 캐싱 토큰을 동기화하는 클래스"""

    def __init__(self, output_dir: Optional[Path] = None):
        """생성자"""
        self.output_dir = output_dir

    def sync_caching_token(self, model_paths: List[Path]) -> List[Path]:
        """
        여러 모델 간 캐싱 토큰을 동기화하는 메서드

        Args:
            model_paths: 동기화할 모델 경로 목록

        Returns:
            처리된 모델 파일 경로 목록 (원본 또는 복사본)
        """
        # 출력 디렉토리가 지정된 경우, 모든 파일을 복사
        processed_paths = []
        working_paths = []

        if self.output_dir:
            for model_path in model_paths:
                copied_path = copy_file_to_output_dir(model_path, self.output_dir)
                processed_paths.append(copied_path)
                working_paths.append(copied_path)
        else:
            # 출력 디렉토리가 없으면 원본 파일 사용
            processed_paths = model_paths.copy()
            working_paths = model_paths.copy()

        # 첫 번째 모델의 토큰 가져오기
        first_token = self.get_caching_token_binary(working_paths[0])
        first_token_bytes = struct.pack("<Q", first_token)  # 정수를 바이트로 변환

        # 나머지 모델에 토큰 적용
        for model_path in working_paths[1:]:
            self.change_param_caching_token(model_path, first_token_bytes)

        return processed_paths

    def get_caching_token_binary(self, model_path: Path) -> int:
        """모델에서 이진 캐싱 토큰을 가져오는 메서드"""
        buf = read_buf(model_path)
        model = Model.Model.GetRootAsModel(buf)
        subgraph = model.Subgraphs(0)
        op = subgraph.Operators(0)
        custom_options_data = bytearray(op.CustomOptionsAsNumpy().tobytes())

        flexbuffer_map = flexbuffers.GetRoot(custom_options_data).AsMap
        executable_content = flexbuffer_map["4"].AsString

        package = Package.Package.GetRootAs(executable_content)

        serial_multi_exec_data = bytearray(package.SerializedMultiExecutableAsNumpy().tobytes())
        multi_executable = MultiExecutable.MultiExecutable.GetRootAs(serial_multi_exec_data)
        executables = {}
        caching_tokens = []
        for i in range(multi_executable.SerializedExecutablesLength()):
            serial_exec = multi_executable.SerializedExecutables(i)
            executable = Executable.Executable.GetRootAs(serial_exec)
            executables[executable.Type()] = executable
            caching_tokens.append(executable.ParameterCachingToken())

        assert len(set(caching_tokens)) == 1, "there is more than two token"

        return caching_tokens[0]

    def get_caching_token(self, model_path: Path) -> bytes:
        """모델에서 캐싱 토큰을 가져오는 메서드"""
        return struct.pack("<Q", self.get_caching_token_binary(model_path))

    def change_param_caching_token(self, model_path: Path, new_token: bytes) -> None:
        """매개변수 캐싱 토큰을 변경하는 메서드"""
        old_token = self.get_caching_token(model_path)
        buf = read_buf(model_path)
        if old_token != new_token:
            while True:
                pointer = find_token_pointer(buf, old_token)
                if pointer == -1:
                    break
                change_token(buf, pointer, new_token)

        save_buf(buf, model_path)


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(description="TFLite 모델 캐싱 토큰 동기화 유틸리티")
    parser.add_argument(
        "--models", type=str, nargs="+", required=True, help="동기화할 TFLite 모델 경로 목록"
    )
    parser.add_argument(
        "--output_dir",
        "-o",
        type=str,
        help="출력 디렉토리 (지정하면 원본을 보존하고 복사본을 수정함)",
        default=None,
    )

    args = parser.parse_args()
    model_paths = [Path(model_path) for model_path in args.models]
    output_dir = Path(args.output_dir) if args.output_dir else None

    token_sync = TfliteTokenSync(output_dir)
    processed_paths = token_sync.sync_caching_token(model_paths)

    if output_dir:
        print(f"{len(model_paths)}개 모델의 캐싱 토큰이 성공적으로 동기화되었습니다.")
        print(f"처리된 파일들이 {output_dir} 디렉토리에 저장되었습니다.")
        for i, path in enumerate(processed_paths):
            print(f"  {i+1}. {path}")
    else:
        print(f"{len(model_paths)}개 모델의 캐싱 토큰이 성공적으로 동기화되었습니다.")


# CLI 인터페이스
if __name__ == "__main__":
    main()
