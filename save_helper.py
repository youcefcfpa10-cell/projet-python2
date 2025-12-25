import json

# دالة لحفظ البيانات في ملف JSON
def save_to_json(data, file_path="data.json"):
    try:
        with open(file_path, "r") as file:
            all_data = json.load(file)
    except FileNotFoundError:
        all_data = {}

    all_data.update(data)  # إضافة أو تحديث البيانات في الملف

    with open(file_path, "w") as file:
        json.dump(all_data, file, ensure_ascii=False, indent=4)
