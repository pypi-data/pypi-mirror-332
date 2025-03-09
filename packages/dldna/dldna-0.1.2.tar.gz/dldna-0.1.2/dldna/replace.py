import os

def rename_imports(root_dir):
    """
    현재 디렉토리와 하위 디렉토리의 모든 Python 파일에서
    'from dldna.'를 'from dldna.'로 변경하고, 변경된 파일과 행 번호를 출력합니다.

    Args:
        root_dir: 탐색을 시작할 루트 디렉토리 경로
    """

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                rename_in_file(filepath)


def rename_in_file(filepath):
    """
    주어진 파일 내에서 'from dldna.'를 'from dldna.'로 변경하고,
    변경된 파일과 행 번호를 출력합니다.

    Args:
        filepath:  변경할 파일의 경로
    """

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()  # 파일 내용을 행 단위로 읽기

        modified = False  # 변경 여부를 추적하는 변수
        modified_lines = []

        for i, line in enumerate(lines):
            original_line = line
            if "from dldna." in line:
                line = line.replace("from dldna.", "from dldna.")
            if "import dldna." in line:
                line = line.replace("import dldna.", "import dldna.")

            if line != original_line:  # 변경된 경우
                modified = True
                modified_lines.append(i + 1)  # 행 번호는 1부터 시작
                lines[i] = line #변경된 행으로 업데이트


        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(lines)  # 변경된 행들을 파일에 쓰기

            print(f"'{filepath}' 파일이 수정되었습니다.")
            print("  변경된 행:", modified_lines)


    except FileNotFoundError:
        print(f"오류: 파일 '{filepath}'을(를) 찾을 수 없습니다.")
    except UnicodeDecodeError:
        print(f"오류: 파일 '{filepath}'을(를) UTF-8로 디코딩할 수 없습니다. 다른 인코딩을 사용해 보세요.")
    except Exception as e:
        print(f"오류: 파일 '{filepath}' 처리 중 예외 발생: {e}")


if __name__ == "__main__":
    root_directory = "."  # 현재 디렉토리
    rename_imports(root_directory)
    print("작업 완료.")