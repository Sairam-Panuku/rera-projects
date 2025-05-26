# rera_scraper.py

projects = [
    {
        "rera_regd_no": "RP/01/2025/01362",
        "project_name": "Basanti Enclave",
        "promoter_name": "M/S. NEELACHAL INFRA DEVELOPERS PVT. LTD",
        "registered_office_address": "Gurudwara, PO-South Balanda, Via: Talcher Rural INR, Angul-759116, Dist. Angul, Odisha",
        "gst_no": "21AADCN5439J2ZH"
    },
    {
        "rera_regd_no": "RP/19/2025/01361",
        "project_name": "UDYAYEEN",
        "promoter_name": "SHYAMCHAND BUILDERS PRIVATE LIMITED",
        "registered_office_address": "MIG-II 21/2 Ground Floor, Chandrasekharpur, Bhubaneswar, Khordha, Odisha, 751016",
        "gst_no": "21ABCCS4755J1ZB"
    },
    {
        "rera_regd_no": "PS/28/2025/01360",
        "project_name": "BARSANA RESIDENCY - II",
        "promoter_name": "RITA PODDAR",
        "registered_office_address": "PLOT NO-2570, PODDAR HEIGHTS, PODDAR COLONY, KHETRAJPUR, Sambalpur, Odisha, 768003",
        "gst_no": "21AREPP3171E1Z7"
    },
    {
        "rera_regd_no": "PS/7/2025/01358",
        "project_name": "KRISHNA MANOR PH-II",
        "promoter_name": "KRISHNA PROPERTIES & DEVELOPERS PRIVATE LIMITED",
        "registered_office_address": "Plot No-46, Indraprastha Housing Colony, Phase-II, Pokhariput, Bhubaneswar, Khordha, Odisha-751020",
        "gst_no": "21AAECK8663L2Z7"
    },
    {
        "rera_regd_no": "PS/19/2025/01351",
        "project_name": "BHAVYAVILLA",
        "promoter_name": "SUNSHINE INFRATECH",
        "registered_office_address": "PLOT NO 339, GOUTAMNAGAR, BJB NAGAR, Khordha, Odisha, 751014",
        "gst_no": "21ACMFS3976P1ZC"
    },
    {
        "rera_regd_no": "RP/19/2025/01355",
        "project_name": "MURALIDHARA HEIGHTS",
        "promoter_name": "TRILOCHAN PROJECTS AND DEVELOPERS PVT. LTD",
        "registered_office_address": "Plot No-208, Flat No-301, Trilochan Plaza, Saheed Nagar, Bhubaneswer, Khordha, Odisha, 751007",
        "gst_no": "21AAGCT0547E1ZT"
    }
]

for i, project in enumerate(projects, start=1):
    print(f"\nProject {i}")
    print("-" * 30)
    for key, value in project.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
