from app import app, db
from app.models.models import *

with app.app_context():

    db.session.query(Course).delete()
    db.session.query(College).delete()
    db.session.commit()

    college_courses = {
        "CEA": [
            "Bachelor of Science in Mechanical Engineering",
            "Bachelor of Science in Architecture (Boni Campus)",
            "Bachelor of Science in Civil Engineering",
            "Bachelor of Science in Electrical Engineering",
            "Bachelor of Science in Electronics Engineering",
            "Bachelor of Science in Computer Engineering",
            "Bachelor of Science in Industrial Engineering (Boni Campus)",
            "Bachelor of Science in Information Technology (Boni Campus)",
            "Bachelor of Science in Instrumentation and Control Engineering (Boni Campus)",
            "Bachelor of Science in Mechatronics",
        ],
        "CBEA": [
            "Bachelor of Science in Accountancy",
            "Bachelor of Science in Entrepreneurship",
            "Bachelor of Science in Office Administration",
            "Bachelor of Science in Business Administration major in Operations Management",
            "Bachelor of Science in Business Administration major in Marketing Management",
            "Bachelor of Science in Business Administration major in Financial Management",
            "Bachelor of Science in Business Administration major in Human Resource Management",
        ],
        "CED": [
            "Bachelor of Secondary Education major in English",
            "Bachelor of Secondary Education major in Math",
            "Bachelor of Secondary Education major in Science (Boni Campus)",
            "Bachelor of Secondary Education major in Social Studies",
            "Bachelor of Secondary Education Major in Filipino",
            "Bachelor of Technical-Vocational Teacher Education major in Animation",
            "Bachelor of Technical-Vocational Teacher Education major in Computer Hardware Servicing",
            "Bachelor of Technical-Vocational Teacher Education major in Visual Graphic Design",
            "Bachelor of Technical-Vocational Teacher Education Major in Garments Fashion and Design",
            "Bachelor of Technical-Vocational Teacher Education Major in Electronics Technology",
            "Bachelor of Technical-Vocational Teacher Education Major in Welding and Fabrications Technology",
            "Bachelor of Technical-Vocational Teacher Education Major in Garments Fashion and Design"
        ],
        "CAS": [
            "Bachelor of Science in Psychology",
            "Bachelor of Arts in Political Science",
            "Bachelor of Science in Statistics (Boni Campus)",
            "Bachelor of Science in Biology (Boni Campus)",
            "Bachelor of Science in Astronomy",
        ],
        "IHK": [
            "Bachelor of Science in Physical Education (Boni Campus)",
        ],
        "Senior High School" : [
            "STEM",
            "ABM",
            "HUMSS",
            "TECH-VOC"
        ],
        "Junior High School" : [
            "SEVEN",
            "EIGHT",
            "NINE",
            "TEN"
        ],
        "Graduate School" : [
            "GRADUATE"
        ]
    }

    for college_name, course_names in college_courses.items():
        college = College(name=college_name)
        db.session.add(college)
        db.session.flush()  # Flush to get the college's ID
        college_id = college.id

        for course_name in course_names:
            course = Course(name=course_name, college_id=college_id)
            db.session.add(course)
            
    db.session.commit()

