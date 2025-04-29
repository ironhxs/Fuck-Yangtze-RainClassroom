from config import filtered_courses
from function.check_in import get_listening_classes_and_sign, check_exam

if __name__ == "__main__":
    get_listening_classes_and_sign(filtered_courses)