student_dict = {
    "student": ["Ryan", "Bob", "Pedro"],
    "score": [80, 81, 82]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

for (key, value) in student_data_frame.items():
    