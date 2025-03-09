from presidio_analyzer import Pattern


patterns = {
    "GLOBAL" : {
        'VISA_CARD': Pattern(name="Visa_Card", regex=r"^(4\d{3}([-\s]?(\d{4})){3})$", score=0.9),
        'MASTER_CARD': Pattern(name="Master_Card", regex=r"^(?:5[1-5]\d{2}|2(2[2-9][1-9]|[3-6]\d{2}|7[01]\d|720))([-\s]?(\d{4})){3}$", score=0.9),
        'AMEX_CARD': Pattern(name="Amex_Card", regex=r"^(3[47]\d{2})([-\s]?)\d{6}\2\d{5}$", score=0.9),
        'RUPAY_CARD': Pattern(name="Rupay_Card", regex=r"^(?:6[05]\d{2}|8[12]\d{2}|508\d|35[36]\d)([-\s]?(\d{4})){3}$", score=0.9),
        'MAESTRO_CARD': Pattern(name="Maestro_Card", regex=r"^(?:5[0678]\d{2}|6013|6[237]\d{2})([-\s]?)\d{4}\1\d{4}\1\d{4}\1\d{0,3}$", score=0.9),
        'IP_ADDRESS': Pattern(name="IP_Address", regex=r"^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){1,6}:([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){1,5}:([0-9A-Fa-f]{1,4}:){1,1}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){1,4}:([0-9A-Fa-f]{1,4}:){1,2}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){1,3}:([0-9A-Fa-f]{1,4}:){1,3}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){1,2}:([0-9A-Fa-f]{1,4}:){1,4}([0-9A-Fa-f]{1,4}|:))|([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:){1,5}([0-9A-Fa-f]{1,4}|:))|(:((:[0-9A-Fa-f]{1,4}){1,6}))|(::(ffff(:0{1,4})?:)?((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|([0-9A-Fa-f]{1,4}:){1,4}:([0-9]{1,3}\.){3}[0-9]{1,3})))$", score=0.9),
        'MAC_ADDRESS': Pattern(name="MAC_Address", regex=r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$|^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$|^[0-9A-Fa-f]{12}$|^([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}$", score=0.80),
        'IFSC': Pattern(name="IFSC", regex=r"^[A-Z]{4}0[A-Z0-9]{6}$", score=0.9),
        'GENDER': Pattern(name="Gender", regex=r"\b(Male|Female|Other|M|F|O)\b", score=0.9),
        'NATIONALITY': Pattern(name="Nationality", regex=r"\b(Indian|American|British|Canadian|Australian|Nationality)\b", score=0.9),
        'ADDRESS': Pattern(name="Address", regex=r"\b\d{1,5}\s\w+\s(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Ln|Lane|Dr|Drive)\b", score=0.9),
        'ZIPCODE': Pattern(name="ZipCode", regex=r"\b\d{5}(-\d{4})?\b", score=0.9),
        'PASSWORD': Pattern(name="Password", regex=r"\b(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}\b", score=0.9),
        'POBOX': Pattern(name="PoBox", regex=r"\bPO Box \d{1,5}\b", score=0.9),
        'PHONE_NUMBER': Pattern(name="Phone", regex=r"\b\d{3}[-. ]?\d{3}[-. ]?\d{4}\b", score=0.9),
        'TITLE': Pattern(name="Title", regex=r"\b(Mr|Mrs|Miss)\b", score=0.9),
        'CVV': Pattern(name="CVV", regex=r"^(?!000$|999$|0000$|9999$)[0-9]{3,4}$", score=0.9),
        'IMEI': Pattern(name="IMEI", regex=r"^\d{2}[-\s]?\d{2}[-\s]?\d{2}[-\s]?\d{2}[-\s]?\d{6}[-\s]?\d{1}$", score=0.9),
        'IMSI': Pattern(name="IMSI", regex=r"^(404|405)(40|44|82|71)\d{10,12}$", score=0.9),
        'EMAIL': Pattern(name="EMAIL", regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", score=0.9),
    },
    "IN" : {
        'UPI_ID': Pattern(name="UPI_ID", regex=r"^[0-9A-Za-z.-]{2,256}@[A-Za-z]{2,64}$", score=0.9),
        'VOTERID': Pattern(name="VoterID", regex=r"^[A-Z]{3}[0-9]{7}$", score=0.9),
        'PASSPORT': Pattern(name="Passport", regex=r"^[A-PR-WY-Z][0-9]{7}$", score=0.9),
        'GST_NUMBER': Pattern(name="GST_Number", regex=r"^\d{2}[A-Z]{5}\d{4}[A-Z]\d[Z][A-Z\d]$", score=0.9),
        'BANK_ACCOUNT_NUMBER': Pattern(name="Bank_Account_Number", regex=r"^\d{9,18}$", score=0.75),
        'DRIVER_LICENSE': Pattern(name="DRIVER_LICENSE", regex=r"^([A-Z]{2}[0-9]{2})([ -])([0-9]{4})[0-9]{7}$", score=0.9),
        'RATION_CARD_NUMBER': Pattern(name="Ration_Card_Number", regex=r"^(AN|AP|AR|AS|BR|CH|CT|DN|DD|DL|GA|GJ|HR|HP|JK|JH|KA|KL|LD|MP|MH|MN|ML|MZ|NL|OR|PY|PB|RJ|SK|TN|TG|TR|UP|UT|UK|WB)[0-9]{10}$", score=0.9),
        'VEHICLE_IDENTIFICATION_NUMBER': Pattern(name="Vehicle_Identification_Number", regex=r"^(AN|AP|AR|AS|BR|CH|CT|DN|DD|DL|GA|GJ|HR|HP|JK|JH|KA|KL|LD|MP|MH|MN|ML|MZ|NL|OR|PY|PB|RJ|SK|TN|TG|TR|UP|UT|UK|WB)[ -]?[0-9]{2}[ -]?[A-Z]{1,2}[ -]?[0-9]{4}$", score=0.9),
        'AADHAAR_CARD': Pattern(name="Aadhaar", regex=r"^([2-9][0-9]{3})([-\s]?(\d{4})){2}$", score=0.85),
        'PAN_CARD': Pattern(name="PAN", regex=r"^[A-Z]{5}[0-9]{4}[A-Z]$", score=0.9),

    }
}

