import json
import logging

class BMI_details:
    bmi = {
       18.4: {
          "category": "Under Weight",
          "health_risk": "Malnutrition Risk"
       },
       24.9: {
          "category": "Normal Weight",
          "health_risk": "Low Risk"
       },
       29.9: {
          "category": "Over Weight",
          "health_risk": "Enhanced Risk"
       },
       34.9: {
          "category": "Moderately Obese",
          "health_risk": "Medium Risk"
       },
       39.9: {
          "category": "Severely Obese",
          "health_risk": "High Risk"
       },
       40: {
          "category": "Very Severely Obese",
          "health_risk": "Very High Risk"
       }
    }

def get_bmi_category_and_risk(bmi_value):
    bmi_values = BMI_details.bmi.keys()
    bmi_values_list = list(bmi_values)
    bmi_values_list.sort()
    for bmi in bmi_values:
        if bmi_value <= bmi:
            return BMI_details.bmi.get(bmi)
    return BMI_details.bmi.get(bmi_values_list[-1])

def calculate_bmi_details(list_of_details):
    logger.info("filtering the unwanted data")
    updated_list_of_details = []
    for entry in list_of_details:
        # filtering data which is in valid format
        if entry["Gender"].isalpha() == True and type(entry["HeightCm"]) == int and type(entry["WeightKg"]) == int:
            height_in_mts = entry["HeightCm"] / 100
            mass = entry["WeightKg"]
            bmi_value = mass / (height_in_mts ** 2)
            category_and_risk = get_bmi_category_and_risk(bmi_value)
            entry["BMI Value"] = bmi_value
            entry["BMI Details"] = category_and_risk
            updated_list_of_details.append(entry)
    return updated_list_of_details

if __name__ == '__main__':

    try:
        # enter the json information into input.json file
        logging.basicConfig(filename="script_logs.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        logger.info("reading the input file")
        f = open('input.json')
        list_of_details = json.load(f)
        logger.info("json file details loaded")
        processed_data = calculate_bmi_details(list_of_details)
        logger.info("Processing completed. Writing formatted data into output.json")
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=4)
        logger.info("Execution completed successfully, please look into output.json file")

    except Exception as e:
        log_file = open('script_logs.log', 'a')
        log_file.write('following exception has occured: ' + e)
        log_file.close()
