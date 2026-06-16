import os

CONDITIONS = {
    "type_2_diabetes": {
        "title": "Type 2 Diabetes",
        "overview": "Type 2 diabetes is a chronic condition in which the body becomes resistant to insulin or does not produce enough insulin, leading to elevated blood sugar levels over time.",
        "symptoms": ["increased thirst", "frequent urination", "fatigue", "blurred vision", "slow-healing sores", "unexplained weight loss"],
        "causes": ["insulin resistance", "excess body weight", "physical inactivity", "family history of diabetes", "age over 45"],
        "treatment": ["lifestyle changes such as diet and exercise", "oral medications to manage blood sugar", "insulin therapy in advanced cases", "regular blood glucose monitoring"],
        "prevention": ["maintaining a healthy weight", "staying physically active", "eating a balanced diet low in refined sugar", "routine health screenings"],
    },
    "hypertension": {
        "title": "Hypertension (High Blood Pressure)",
        "overview": "Hypertension is a common condition in which the long-term force of blood against artery walls is high enough that it may eventually cause health problems such as heart disease.",
        "symptoms": ["often no symptoms", "headaches in severe cases", "shortness of breath", "nosebleeds", "dizziness"],
        "causes": ["high salt intake", "obesity", "lack of physical activity", "excessive alcohol consumption", "chronic stress", "genetics"],
        "treatment": ["dietary sodium reduction", "regular exercise", "antihypertensive medications", "weight management", "stress reduction techniques"],
        "prevention": ["limiting salt and processed foods", "maintaining a healthy weight", "regular physical activity", "limiting alcohol intake", "routine blood pressure checks"],
    },
    "asthma": {
        "title": "Asthma",
        "overview": "Asthma is a chronic respiratory condition in which the airways narrow and swell, producing extra mucus, which can make breathing difficult and trigger coughing or wheezing.",
        "symptoms": ["wheezing", "shortness of breath", "chest tightness", "coughing, especially at night or early morning"],
        "causes": ["allergens such as pollen or dust mites", "respiratory infections", "physical activity in some cases", "cold air", "air pollutants and irritants"],
        "treatment": ["inhaled bronchodilators for quick relief", "inhaled corticosteroids for long-term control", "avoiding known triggers", "an individualized asthma action plan"],
        "prevention": ["identifying and avoiding personal triggers", "getting recommended vaccinations", "monitoring breathing with a peak flow meter", "following a prescribed control plan"],
    },
    "seasonal_allergies": {
        "title": "Seasonal Allergies (Allergic Rhinitis)",
        "overview": "Seasonal allergies occur when the immune system overreacts to airborne substances such as pollen, leading to inflammation of the nasal passages.",
        "symptoms": ["sneezing", "runny or stuffy nose", "itchy or watery eyes", "postnasal drip", "fatigue"],
        "causes": ["pollen from trees, grasses, and weeds", "mold spores", "genetic predisposition to allergies"],
        "treatment": ["antihistamines", "nasal corticosteroid sprays", "decongestants for short-term relief", "allergen immunotherapy for persistent cases"],
        "prevention": ["checking pollen forecasts and limiting outdoor exposure", "keeping windows closed during high pollen counts", "showering after outdoor activity", "using air filters indoors"],
    },
    "migraine": {
        "title": "Migraine",
        "overview": "A migraine is a neurological condition characterized by intense, debilitating headaches often accompanied by nausea, sensitivity to light, and visual disturbances.",
        "symptoms": ["throbbing head pain, often on one side", "nausea or vomiting", "sensitivity to light and sound", "visual aura in some cases"],
        "causes": ["hormonal changes", "certain foods and food additives", "stress", "sleep disturbances", "sensory stimuli such as bright lights"],
        "treatment": ["over-the-counter or prescription pain relievers", "triptans for acute attacks", "preventive medications for frequent migraines", "rest in a dark, quiet room"],
        "prevention": ["identifying and avoiding personal triggers", "maintaining a regular sleep schedule", "managing stress", "staying hydrated"],
    },
    "common_cold": {
        "title": "Common Cold",
        "overview": "The common cold is a viral infection of the upper respiratory tract that is generally mild and resolves on its own within a week or two.",
        "symptoms": ["runny or stuffy nose", "sore throat", "cough", "mild fatigue", "low-grade fever in some cases"],
        "causes": ["rhinoviruses and other respiratory viruses", "close contact with an infected person", "weakened immune defenses"],
        "treatment": ["rest and adequate fluids", "over-the-counter cold medications for symptom relief", "throat lozenges for sore throat", "humidifiers to ease congestion"],
        "prevention": ["frequent handwashing", "avoiding close contact with sick individuals", "not touching the face with unwashed hands", "maintaining overall good health"],
    },
    "influenza": {
        "title": "Influenza",
        "overview": "Influenza, or the flu, is a contagious respiratory illness caused by influenza viruses that can range from mild to severe and occasionally lead to serious complications.",
        "symptoms": ["fever or chills", "muscle aches", "fatigue", "cough", "sore throat", "headache"],
        "causes": ["infection with influenza A or B viruses", "airborne transmission through droplets", "contact with contaminated surfaces"],
        "treatment": ["rest and fluids", "antiviral medications if started early", "fever reducers and pain relievers", "monitoring for complications"],
        "prevention": ["annual flu vaccination", "frequent handwashing", "avoiding close contact with sick individuals", "covering coughs and sneezes"],
    },
    "gerd": {
        "title": "Gastroesophageal Reflux Disease (GERD)",
        "overview": "GERD is a digestive disorder in which stomach acid frequently flows back into the esophagus, irritating its lining and causing recurring discomfort.",
        "symptoms": ["heartburn", "regurgitation of food or sour liquid", "chest discomfort", "difficulty swallowing", "chronic cough"],
        "causes": ["a weakened lower esophageal sphincter", "obesity", "hiatal hernia", "certain foods and large meals", "smoking"],
        "treatment": ["lifestyle and dietary modifications", "antacids and acid-reducing medications", "elevating the head during sleep", "weight management"],
        "prevention": ["avoiding trigger foods such as spicy or fatty meals", "eating smaller, more frequent meals", "not lying down soon after eating", "maintaining a healthy weight"],
    },
    "generalized_anxiety_disorder": {
        "title": "Generalized Anxiety Disorder",
        "overview": "Generalized anxiety disorder involves persistent and excessive worry about everyday situations that is difficult to control and interferes with daily functioning.",
        "symptoms": ["excessive worry", "restlessness", "difficulty concentrating", "muscle tension", "sleep disturbances", "irritability"],
        "causes": ["genetic predisposition", "brain chemistry differences", "chronic stress", "traumatic life events"],
        "treatment": ["cognitive behavioral therapy", "anti-anxiety or antidepressant medications", "relaxation techniques", "regular physical activity"],
        "prevention": ["stress management practices", "limiting caffeine and stimulant intake", "maintaining social support networks", "seeking early professional support"],
    },
    "iron_deficiency_anemia": {
        "title": "Iron Deficiency Anemia",
        "overview": "Iron deficiency anemia occurs when the body lacks enough iron to produce adequate hemoglobin, reducing the blood's ability to carry oxygen efficiently.",
        "symptoms": ["fatigue", "pale skin", "shortness of breath", "dizziness", "brittle nails", "cold hands and feet"],
        "causes": ["insufficient dietary iron intake", "blood loss from menstruation or internal bleeding", "poor iron absorption", "pregnancy"],
        "treatment": ["iron supplements as advised by a doctor", "dietary changes to increase iron intake", "treating underlying causes of blood loss"],
        "prevention": ["eating iron-rich foods such as leafy greens and lean meats", "pairing iron-rich foods with vitamin C", "routine blood testing for at-risk individuals"],
    },
    "hypothyroidism": {
        "title": "Hypothyroidism",
        "overview": "Hypothyroidism is a condition in which the thyroid gland does not produce enough thyroid hormone, slowing down the body's metabolism.",
        "symptoms": ["fatigue", "weight gain", "cold intolerance", "dry skin", "hair thinning", "depression"],
        "causes": ["autoimmune thyroid disease", "iodine deficiency", "thyroid surgery or radiation treatment", "certain medications"],
        "treatment": ["daily thyroid hormone replacement therapy", "regular monitoring of thyroid hormone levels", "dosage adjustments as needed"],
        "prevention": ["adequate dietary iodine intake", "routine thyroid screening for at-risk individuals", "monitoring symptoms after thyroid-related treatments"],
    },
    "osteoarthritis": {
        "title": "Osteoarthritis",
        "overview": "Osteoarthritis is a degenerative joint disease in which the protective cartilage that cushions the ends of bones gradually wears down over time.",
        "symptoms": ["joint pain and stiffness", "reduced range of motion", "swelling around the joint", "a grating sensation during movement"],
        "causes": ["aging", "joint injury", "obesity", "repetitive joint stress", "genetic factors"],
        "treatment": ["physical therapy", "pain relief medications", "weight management", "joint injections in moderate cases", "joint replacement surgery in severe cases"],
        "prevention": ["maintaining a healthy weight", "low-impact exercise to strengthen muscles around joints", "avoiding repetitive joint strain", "proper injury care"],
    },
    "atopic_dermatitis": {
        "title": "Eczema (Atopic Dermatitis)",
        "overview": "Atopic dermatitis is a chronic skin condition that causes the skin to become dry, itchy, and inflamed, often beginning in childhood.",
        "symptoms": ["dry, scaly skin", "intense itching", "red or brownish-gray patches", "small raised bumps that may leak fluid"],
        "causes": ["genetic factors affecting the skin barrier", "immune system overactivity", "environmental irritants", "allergens"],
        "treatment": ["regular moisturizing", "topical corticosteroids for flare-ups", "avoiding known irritants", "antihistamines for itching"],
        "prevention": ["using gentle, fragrance-free skin products", "moisturizing daily", "avoiding harsh soaps and hot showers", "identifying and avoiding personal triggers"],
    },
    "urinary_tract_infection": {
        "title": "Urinary Tract Infection",
        "overview": "A urinary tract infection is a bacterial infection affecting any part of the urinary system, most commonly the bladder and urethra.",
        "symptoms": ["a strong, persistent urge to urinate", "burning sensation during urination", "cloudy or strong-smelling urine", "pelvic discomfort"],
        "causes": ["bacteria entering the urinary tract", "incomplete bladder emptying", "certain types of birth control", "structural urinary tract issues"],
        "treatment": ["antibiotics prescribed by a doctor", "increased fluid intake", "pain relief for discomfort"],
        "prevention": ["staying well hydrated", "urinating after sexual activity", "wiping front to back", "avoiding irritating feminine products"],
    },
    "insomnia": {
        "title": "Insomnia",
        "overview": "Insomnia is a sleep disorder characterized by persistent difficulty falling asleep, staying asleep, or both, leading to impaired daytime functioning.",
        "symptoms": ["difficulty falling asleep", "waking up frequently during the night", "waking too early", "daytime fatigue and irritability"],
        "causes": ["stress and anxiety", "irregular sleep schedules", "excessive caffeine or screen use before bed", "underlying medical or mental health conditions"],
        "treatment": ["cognitive behavioral therapy for insomnia", "good sleep hygiene practices", "short-term medication in some cases", "addressing underlying conditions"],
        "prevention": ["maintaining a consistent sleep schedule", "limiting caffeine and screen time before bed", "creating a comfortable, dark sleep environment", "regular physical activity"],
    },
    "chronic_bronchitis": {
        "title": "Chronic Bronchitis",
        "overview": "Chronic bronchitis is a long-term inflammation of the bronchial tubes that leads to persistent coughing and excess mucus production.",
        "symptoms": ["persistent cough with mucus", "shortness of breath", "wheezing", "chest discomfort", "frequent respiratory infections"],
        "causes": ["long-term tobacco smoke exposure", "air pollution", "occupational dust and chemical exposure", "repeated respiratory infections"],
        "treatment": ["smoking cessation", "bronchodilator inhalers", "pulmonary rehabilitation", "avoiding lung irritants"],
        "prevention": ["avoiding tobacco smoke", "reducing exposure to air pollutants", "getting recommended vaccinations", "practicing good respiratory hygiene"],
    },
    "vitamin_d_deficiency": {
        "title": "Vitamin D Deficiency",
        "overview": "Vitamin D deficiency occurs when the body does not get or produce enough vitamin D, which is essential for bone health and immune function.",
        "symptoms": ["fatigue", "bone pain", "muscle weakness", "frequent illness", "mood changes"],
        "causes": ["limited sun exposure", "insufficient dietary intake", "certain medical conditions affecting absorption", "darker skin pigmentation reducing synthesis"],
        "treatment": ["vitamin D supplementation as advised by a doctor", "increased safe sun exposure", "dietary changes to include vitamin D rich foods"],
        "prevention": ["regular safe sun exposure", "eating vitamin D rich foods such as fatty fish and fortified products", "routine screening for at-risk individuals"],
    },
    "plantar_fasciitis": {
        "title": "Plantar Fasciitis",
        "overview": "Plantar fasciitis is inflammation of the thick band of tissue running across the bottom of the foot, commonly causing heel pain.",
        "symptoms": ["sharp heel pain, especially with first steps in the morning", "pain after long periods of standing", "stiffness in the foot"],
        "causes": ["repetitive strain on the foot", "improper footwear", "obesity", "tight calf muscles", "high-impact activities"],
        "treatment": ["rest and ice therapy", "stretching exercises", "supportive footwear or orthotics", "physical therapy"],
        "prevention": ["wearing supportive shoes", "stretching before physical activity", "maintaining a healthy weight", "gradually increasing exercise intensity"],
    },
    "tension_headache": {
        "title": "Tension Headache",
        "overview": "A tension headache is the most common type of headache, typically causing a dull, aching pain and tightness across the forehead or scalp.",
        "symptoms": ["dull, pressing pain", "tightness around the head", "tenderness in the scalp, neck, or shoulders", "mild to moderate intensity"],
        "causes": ["stress", "poor posture", "eye strain", "muscle tension", "lack of sleep"],
        "treatment": ["over-the-counter pain relievers", "stress management techniques", "improved posture", "regular breaks from screen use"],
        "prevention": ["managing stress levels", "maintaining good posture", "taking regular breaks during screen-heavy tasks", "staying well hydrated"],
    },
    "sinusitis": {
        "title": "Sinusitis",
        "overview": "Sinusitis is inflammation of the sinuses, often caused by infection, that leads to congestion, facial pressure, and other discomforts.",
        "symptoms": ["facial pain or pressure", "nasal congestion", "thick nasal discharge", "reduced sense of smell", "headache"],
        "causes": ["viral or bacterial infection", "allergies", "nasal polyps", "structural nasal issues"],
        "treatment": ["saline nasal rinses", "decongestants", "antibiotics for bacterial cases", "corticosteroid nasal sprays"],
        "prevention": ["managing seasonal allergies", "practicing good hand hygiene", "using a humidifier", "avoiding known irritants"],
    },
}


def build_document_text(condition):
    lines = [
        f"# {condition['title']}",
        "",
        "## Overview",
        condition["overview"],
        "",
        "## Common Symptoms",
        "\n".join(f"- {item.capitalize()}" for item in condition["symptoms"]),
        "",
        "## Causes",
        "\n".join(f"- {item.capitalize()}" for item in condition["causes"]),
        "",
        "## Treatment Options",
        "\n".join(f"- {item.capitalize()}" for item in condition["treatment"]),
        "",
        "## Prevention Tips",
        "\n".join(f"- {item.capitalize()}" for item in condition["prevention"]),
        "",
        "## When to See a Doctor",
        f"Consult a licensed healthcare provider if symptoms of {condition['title'].lower()} are severe, persistent, or worsening, or if you are uncertain about the right course of action. This document is for general informational purposes only and is not a substitute for professional medical advice.",
    ]
    return "\n".join(lines)


def generate_documents(output_dir="data/medical_documents"):
    os.makedirs(output_dir, exist_ok=True)
    for filename, condition in CONDITIONS.items():
        text = build_document_text(condition)
        with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    return len(CONDITIONS)


if __name__ == "__main__":
    count = generate_documents()
    print(f"Generated {count} medical reference documents")
