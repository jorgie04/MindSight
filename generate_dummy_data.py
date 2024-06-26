# Generates 200 dummy records for testing

import os
import random
from datetime import date, timedelta
from faker import Faker
from app import db, app
from app.models.models import *
from dummy_data_input import *

with app.app_context():

    # db.session.query(PersonalInformation).delete()
    db.session.query(Sibling).delete()
    db.session.query(Conviction).delete()
    db.session.query(CaseNote).delete()
    db.session.query(ReferralInformation).delete()
    db.session.query(FamilyBackground).delete()
    db.session.query(HealthInformation).delete()
    db.session.query(EducationalBackground).delete()
    db.session.query(Sessions).delete()
    db.session.query(HistoryInformation).delete()
    db.session.query(SocialHistory).delete()
    db.session.query(OccupationalHistory).delete()
    db.session.query(SubstanceAbuseHistory).delete()
    db.session.query(LegalHistory).delete()
    db.session.query(AdditionalInformation).delete()
    db.session.query(Document).delete()
    db.session.query(BasicInformation).delete()
    db.session.commit()

    fake = Faker()

    def random_date(start_date, end_date):
        return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    def generate_student_id():
        year = random.randint(2020, 2023)
        student_number = str(random.randint(100000, 200000)).zfill(6)
        student_id = str(year) + "-" + str(student_number)
        print(f"Generated Student ID: {student_id}")
        return student_id

    # def generate_fake_student_visit(student):
    #     visit = Sessions(
    #         student=student,
    #         date_of_visit=random_date(date(2020, 1, 1), date(2023, 12, 31)),
    #         nature_of_concern=fake.random_element(elements=["Academic", "Career", "Personal", "Social"])
    #     )
    #     db.session.add(visit)

    start_date = datetime(2021, 1, 1)
    end_date = datetime(2024, 12, 31)

    def pick_course(college):
        course_prefix = college.lower()

        if course_prefix in course_lists:
            course_var = course_lists[course_prefix]
            
            return random.choice(course_var)
        else:
            return None

    for _ in range(100):
        family_name = fake.last_name()
        college = fake.random_element(elements=college_names)

        student = BasicInformation(
            student_id=generate_student_id(),
            last_name=family_name,
            first_name=fake.first_name(),
            college=college,
            course=pick_course(college),
            # gpa=round(random.uniform(1.0, 5.0), 2),
            campus=fake.random_element(elements=["Boni", "Pasig"]),
            age=random.randint(18, 30),
            gender=fake.random_element(elements=("Male", "Female", "LGBTQIA+")),
            contact_number=fake.random_int(min=100000, max=99999999999),
            religion=fake.random_element(elements=religion_names),
            date_of_birth=random_date(date(1990, 1, 1), date(2005, 1, 1)),
            nationality=fake.random_element(elements=("Filipino", "Non-Filipino")),
            residence=fake.random_element(elements=("Family Home", "Guardian's Home", "School Dormitory", "Dormitory", "Others")),
            email_address=fake.email(),
            civil_status=fake.random_element(elements=("Single", "Married", "Divorced", "Widowed")),
            submitted_on=fake.date_time_between(start_date=start_date, end_date=end_date),
            student_signature=os.urandom(1000)
        )
        
        if college in ["CEA", "CBEA", "CAS", "CED", "IHK"]:
            student.year_level = str(random.randint(1, 4))
        elif college == "JHS":
            student.year_level = str(random.randint(7, 10))
        elif college == "SHS":
            student.year_level = str(random.randint(11, 12))
        else:
            student.year_level = None

        db.session.add(student)
        db.session.commit()

        history_information = HistoryInformation(
            information_provider=fake.name(),
            current_problem=fake.sentence(),
            problem_length=fake.sentence(),
            stressors=fake.sentence(),
            substance_abuse=fake.boolean(),
            addiction=fake.boolean(),
            depression_sad_down_feelings=fake.boolean(),
            high_low_energy_level=fake.boolean(),
            angry_irritable=fake.boolean(),
            loss_of_interest=fake.boolean(),
            difficulty_enjoying_things=fake.boolean(),
            crying_spells=fake.boolean(),
            decreased_motivation=fake.boolean(),
            withdrawing_from_people=fake.boolean(),
            mood_swings=fake.boolean(),
            black_and_white_thinking=fake.boolean(),
            negative_thinking=fake.boolean(),
            change_in_weight_or_appetite=fake.boolean(),
            change_in_sleeping_pattern=fake.boolean(),
            suicidal_thoughts_or_plans=fake.boolean(),
            self_harm=fake.boolean(),
            homicidal_thoughts_or_plans=fake.boolean(),
            difficulty_focusing=fake.boolean(),
            feelings_of_hopelessness=fake.boolean(),
            feelings_of_shame_or_guilt=fake.boolean(),
            feelings_of_inadequacy=fake.boolean(),
            anxious_nervous_tense_feelings=fake.boolean(),
            panic_attacks=fake.boolean(),
            racing_or_scrambled_thoughts=fake.boolean(),
            bad_or_unwanted_thoughts=fake.boolean(),
            flashbacks_or_nightmares=fake.boolean(),
            muscle_tensions_aches=fake.boolean(),
            hearing_voices_or_seeing_things=fake.boolean(),
            thoughts_of_running_away=fake.boolean(),
            paranoid_thoughts=fake.boolean(),
            feelings_of_frustration=fake.boolean(),
            feelings_of_being_cheated=fake.boolean(),
            perfectionism=fake.boolean(),
            counting_washing_checking=fake.boolean(),
            distorted_body_image=fake.boolean(),
            concerns_about_dieting=fake.boolean(),
            loss_of_control_over_eating=fake.boolean(),
            binge_eating_or_purging=fake.boolean(),
            rules_about_eating=fake.boolean(),
            compensating_for_eating=fake.boolean(),
            excessive_exercise=fake.boolean(),
            indecisiveness_about_career=fake.boolean(),
            job_problems=fake.boolean(),
            other=fake.sentence(),
            previous_treatments=fake.random_element(elements=("Yes", "No")),
            previous_treatments_likes_dislikes=fake.sentence(),
            previous_treatments_learned=fake.sentence(),
            previous_treatments_like_to_continue=fake.sentence(),
            previous_hospital_stays_psych=fake.boolean(),
            current_thoughts_to_harm=fake.random_element(elements=("Yes", "No")),
            past_thoughts_to_harm=fake.random_element(elements=("Yes", "No")),
            student_id=student.student_id
        )

        health_information = HealthInformation(
            medication_and_dose=fake.sentence(),
            serious_ch_illnesses_history=fake.sentence(),
            head_injuries=fake.random_element(elements=("Yes", "No")),
            lose_consciousness=fake.random_element(elements=("Yes", "No")),
            convulsions_or_seizures=fake.random_element(elements=("Yes", "No")),
            fever=fake.random_element(elements=("Yes", "No")),
            allergies=fake.random_element(elements=("Yes", "No")),
            current_physical_health=fake.sentence(nb_words=1),
            last_check_up=random_date(date(2020, 1, 1), date(2023, 12, 31)),
            has_physician=fake.random_element(elements=("Yes", "No")),
            physician_name=fake.name(),
            physician_email=fake.email(),
            physician_number = fake.random_int(min=100000, max=99999999999),
            student=student
        )

        family_background = FamilyBackground(
            birth_location = fake.city(),
            raised_by = fake.name(),

            #TODO: CHANGE 
            rel_qual_mother = fake.sentence(nb_words=1),
            rel_qual_father = fake.sentence(nb_words=1),
            rel_qual_step_parent = fake.sentence(nb_words=1),

            family_abuse_history=fake.sentence(),
            family_mental_history=fake.sentence(),
            additional_information=fake.sentence(),
            student=student
        )

        social_history = SocialHistory(
            relationship_with_peers=fake.sentence(),
            social_support_network=fake.sentence(),
            hobbies_or_interests=fake.sentence(),
            cultural_concerns=fake.sentence(),
            student = student
        )

        educational_background = EducationalBackground(
            educational_history=fake.sentence(nb_words=3),
            highest_level_achieved=fake.sentence(nb_words=3),
            additional_information=fake.sentence(nb_words=3),
            student=student
        )

        occupational_history = OccupationalHistory(
            employment_status=fake.sentence(nb_words=1),
            satisfaction=fake.sentence(nb_words=1),
            satisfaction_reason=fake.sentence(nb_words=1),
            student = student
        )

        substance_abuse_history = SubstanceAbuseHistory(
            struggled_with_substance_abuse=fake.random_element(elements=("Yes", "No")),
            alcohol=fake.random_element(elements=("Yes", "No")),
            alcohol_age_first_use = fake.sentence(nb_words=2),
            alcohol_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            alcohol_amount_used = fake.sentence(nb_words=2),
            alcohol_way_of_intake = fake.sentence(nb_words=2),
            cigarette = fake.random_element(elements=("Yes", "No")),
            cigarette_age_first_use = fake.sentence(nb_words=2),
            cigarette_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            cigarette_amount_used = fake.sentence(nb_words=2),
            cigarette_way_of_intake = fake.sentence(nb_words=2),
            marijuana = fake.random_element(elements=("Yes", "No")),
            marijuana_age_first_use = fake.sentence(nb_words=2),
            marijuana_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            marijuana_amount_used = fake.sentence(nb_words=2),
            marijuana_way_of_intake = fake.sentence(nb_words=2),
            cocaine = fake.random_element(elements=("Yes", "No")),
            cocaine_age_first_use = fake.sentence(nb_words=2),
            cocaine_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            cocaine_amount_used = fake.sentence(nb_words=2),
            cocaine_way_of_intake = fake.sentence(nb_words=2),
            heroin = fake.random_element(elements=("Yes", "No")),
            heroin_age_first_use = fake.sentence(nb_words=2),
            heroin_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            heroin_amount_used = fake.sentence(nb_words=2),
            heroin_way_of_intake = fake.sentence(nb_words=2),
            amphetamines = fake.random_element(elements=("Yes", "No")),
            amphetamines_age_first_use = fake.sentence(nb_words=2),
            amphetamines_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            amphetamines_amount_used = fake.sentence(nb_words=2),
            amphetamines_way_of_intake = fake.sentence(nb_words=2),
            club_drugs = fake.random_element(elements=("Yes", "No")),
            club_drugs_age_first_use = fake.sentence(nb_words=2),
            club_drugs_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            club_drugs_amount_used = fake.sentence(nb_words=2),
            club_drugs_way_of_intake = fake.sentence(nb_words=2),
            pain_meds = fake.random_element(elements=("Yes", "No")),
            pain_meds_age_first_use = fake.sentence(nb_words=2),
            pain_meds_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            pain_meds_amount_used = fake.sentence(nb_words=2),
            pain_meds_way_of_intake = fake.sentence(nb_words=2),
            benzo = fake.random_element(elements=("Yes", "No")),
            benzo_age_first_use = fake.sentence(nb_words=2),
            benzo_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            benzo_amount_used = fake.sentence(nb_words=2),
            benzo_way_of_intake = fake.sentence(nb_words=2),
            hallucinogens = fake.random_element(elements=("Yes", "No")),
            hallucinogens_age_first_use = fake.sentence(nb_words=2),
            hallucinogens_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            hallucinogens_amount_used = fake.sentence(nb_words=2),
            hallucinogens_way_of_intake = fake.sentence(nb_words=2),
            other_meds = fake.random_element(elements=("Yes", "No")),
            other_meds_age_first_use = fake.sentence(nb_words=2),
            other_meds_frequency_of_use = fake.random_element(elements=("Daily", "Weekly", "Monthly")),
            other_meds_amount_used = fake.sentence(nb_words=2),
            other_meds_way_of_intake = fake.sentence(nb_words=2),

            treatment_program_name = fake.sentence(nb_words=2),
            treatment_type = fake.sentence(nb_words=2),
            treatment_date = fake.date(),
            treatment_outcome = fake.sentence(nb_words=2),

            student = student
        )

        legal_history = LegalHistory(
            pending_criminal_charges=fake.random_element(elements=("Yes", "No")),
            on_probation=fake.random_element(elements=("Yes", "No")),
            has_been_arrested=fake.random_element(elements=("Yes", "No")),

            student = student
        )

        additional_information = AdditionalInformation(
            to_work_on=fake.sentence(),
            expectations=fake.sentence(),
            things_to_change=fake.sentence(),
            other_information=fake.sentence(),
            nature_of_concern=fake.random_element(elements=("Academic","Personal","Career","Social")),
            personal_agreement = True,
            personal_agreement_date=fake.date_time_between(start_date=start_date, end_date=end_date),
            counselor=fake.random_element(elements=("Emmanuelle Santiago","Russel Ane Dela Cruz","Jake Jason Queddeng","Lizelle Anne Manabat")),
            status=fake.random_element(elements=("Active","Terminated")),
            remarks=fake.random_element(elements=("For Follow-Up","For Outside Referral","Case Reopen")),

            student = student

        )

        # for _ in range(1):
        #     generate_fake_student_visit(student)

        # db.session.add(personal_information)
        db.session.add(history_information)
        db.session.add(health_information)
        db.session.add(family_background)
        db.session.add(social_history)
        db.session.add(educational_background)
        db.session.add(occupational_history)
        db.session.add(substance_abuse_history)
        db.session.add(legal_history)
        db.session.add(additional_information)

        db.session.commit()

    db.session.close()
