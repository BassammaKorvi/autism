import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/chanu/PycharmProjects/ASD/Autistic_Spectrum_Disorder.pkl', 'rb'))

# creating a function for Prediction
def asd_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction


def main():
    # giving a title
    st.title('Autism Spectrum Disorder Detection')
    # Define the options for the dropdown
    options = ["yes", "no"]

    # Create the dropdowns for each question and store the selected values in variables
    answer1 = st.selectbox("Does your child look at you when you call his/her name?", options)
    answer2 = st.selectbox("How easy is it for you to get eye contact with your child?", options)
    answer3 = st.selectbox(
        "Does your child point to indicate that s/he wants something? (e.g. a toy that is out of reach)", options)
    answer4 = st.selectbox("Does your child point to share interest with you? (e.g. pointing at an interesting sight)",
                           options)
    answer5 = st.selectbox("Does your child pretend? (e.g. care for dolls, talk on a toy phone)", options)
    answer6 = st.selectbox("Does your child follow where you’re looking?", options)
    answer7 = st.selectbox(
        "If you or someone else in the family is visibly upset, does your child show signs of wanting to comfort them? (e.g. stroking hair, hugging them)",
        options)
    answer8 = st.selectbox("Would you describe your child’s first words as:", options)
    answer9 = st.selectbox("Does your child use simple gestures? (e.g. wave goodbye)", options)
    answer10 = st.selectbox("Does your child stare at nothing with no apparent purpose?", options)

    # Convert the answers to 1 or 0
    a1_value = 1 if answer1 == "yes" else 0
    a2_value = 1 if answer2 == "yes" else 0
    a3_value = 1 if answer3 == "yes" else 0
    a4_value = 1 if answer4 == "yes" else 0
    a5_value = 1 if answer5 == "yes" else 0
    a6_value = 1 if answer6 == "yes" else 0
    a7_value = 1 if answer7 == "yes" else 0
    a8_value = 1 if answer8 == "yes" else 0
    a9_value = 1 if answer9 == "yes" else 0
    a10_value = 1 if answer10 == "yes" else 0

    # getting the input data from the user
    A1 = a1_value
    A2 = a2_value
    A3 = a3_value
    A4 = a4_value
    A5 = a5_value
    A6 = a6_value
    A7 = a7_value
    A8 = a8_value
    A9 = a9_value
    A10 = a10_value

    age_input = st.text_input('Age_Months')
    if age_input:
        Age_Months = float(age_input)
    else:
        Age_Months = 0

    sex_map = {"m": 1, "f": 0}
    sex = st.selectbox('Sex', options=list(sex_map.keys()), index=0)
    Sex = sex_map.get(sex, 0)

    ethnicity_map = {
        "middle eastern": 8,
        "White European": 5,
        "Hispanic": 0,
        "black": 7,
        "asian": 6,
        "south asian": 10,
        "Native Indian": 2,
        "Others": 3,
        "Latino": 1,
        "mixed": 9,
        "Pacifica": 4
    }
    ethnicity = st.selectbox('Ethnicity', options=list(ethnicity_map.keys()), index=0)
    Ethnicity = ethnicity_map.get(ethnicity, 0)

    jaundice_map = {"yes": 1, "no": 0}
    jaundice =st.selectbox('Jaundice', options=list(jaundice_map.keys()), index=0)
    Jaundice = jaundice_map.get(jaundice, 0)

    family_map = {"yes": 1, "no": 0}
    family_Member_with_ASD =st.selectbox('Family_Member_with_ASD', options=list(family_map.keys()), index=0)
    Family_Member_with_ASD = family_map.get(family_Member_with_ASD, 0)

    who_map = {"family member": 0, "Health Care Professional": 1, "self": 2, "others": 3}
    who = st.selectbox('Who Completed the Test', options=list(who_map.keys()), index=0)
    Who_completed_the_test = who_map.get(who, 0)

    # code for Prediction
    asd__prediction = ' '

    # creating a button for Prediction

    if st.button('Prediction'):
        asd__prediction = asd_prediction(
            [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, Age_Months, Sex, Ethnicity, Jaundice, Family_Member_with_ASD,
             Who_completed_the_test])

    st.success(asd__prediction)


if __name__ == '__main__':
    main()
