# Araca özel dinamik özellikler ve uyumluluk verileri (Marka -> Seri -> Model -> Özellikler)
CAR_DATA = {
    "Fiat": {
        "Egea": {
            "1.4 Fire / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP"],
                "years": [str(y) for y in range(2015, 2024)],
                "oil": "5W-40",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            },
            "1.3 Multijet / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP"],
                "years": [str(y) for y in range(2015, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            },
            "1.6 Multijet / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["120 HP", "130 HP"],
                "years": [str(y) for y in range(2015, 2024)],
                "oil": "0W-30",
                "battery": "72 Ah",
                "tire": "225/45 R17"
            }
        },
        "Linea": {
            "1.3 Multijet / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP"],
                "years": [str(y) for y in range(2007, 2018)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            },
            "1.6 Multijet / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["105 HP"],
                "years": [str(y) for y in range(2009, 2016)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/55 R16"
            }
        },
        "Fiorino": {
            "1.3 Multijet / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP", "95 HP"],
                "years": [str(y) for y in range(2008, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "Doblo": {
            "1.6 Multijet / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["105 HP", "120 HP"],
                "years": [str(y) for y in range(2010, 2023)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/60 R16"
            },
            "1.3 Multijet / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2005, 2015)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "Şahin/Doğan": {
            "1.6 OHV / Benzin-LPG": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel"],
                "powers": ["80 HP"],
                "years": [str(y) for y in range(1990, 2003)],
                "oil": "20W-50",
                "battery": "60 Ah",
                "tire": "175/70 R13"
            }
        },
        "Kartal": {
            "1.6 OHV / Benzin-LPG": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel"],
                "powers": ["80 HP"],
                "years": [str(y) for y in range(1990, 2003)],
                "oil": "20W-50",
                "battery": "60 Ah",
                "tire": "175/70 R13"
            }
        }
    },
    "Renault": {
        "Clio IV": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2012, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/55 R16"
            }
        },
        "Clio V": {
            "1.0 TCe / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP", "100 HP"],
                "years": [str(y) for y in range(2019, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/55 R16"
            }
        },
        "Megane IV": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["110 HP", "115 HP"],
                "years": [str(y) for y in range(2016, 2024)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.3 TCe / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["140 HP"],
                "years": [str(y) for y in range(2018, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            }
        },
        "Symbol": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["85 HP"],
                "years": [str(y) for y in range(2008, 2014)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "175/65 R14"
            },
            "1.2 16V / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP"],
                "years": [str(y) for y in range(2008, 2014)],
                "oil": "10W-40",
                "battery": "50 Ah",
                "tire": "175/65 R14"
            }
        },
        "Fluence": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["110 HP"],
                "years": [str(y) for y in range(2009, 2017)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/60 R16"
            }
        },
        "R9 Broadway": {
            "1.4 / Benzin-LPG": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel"],
                "powers": ["72 HP"],
                "years": [str(y) for y in range(1985, 2001)],
                "oil": "20W-50",
                "battery": "60 Ah",
                "tire": "175/70 R13"
            }
        },
        "R19 Europa": {
            "1.6 / Benzin-LPG": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(1996, 2002)],
                "oil": "10W-40",
                "battery": "60 Ah",
                "tire": "175/70 R13"
            }
        },
        "Kangoo": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP", "110 HP"],
                "years": [str(y) for y in range(2008, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/65 R15"
            }
        }
    },
    "Volkswagen": {
        "Passat B8": {
            "1.6 TDI / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["120 HP"],
                "years": [str(y) for y in range(2015, 2021)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "215/55 R17"
            },
            "1.4 TSI / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["125 HP", "150 HP"],
                "years": [str(y) for y in range(2015, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "215/55 R17"
            }
        },
        "Passat B7": {
            "1.6 TDI / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["105 HP"],
                "years": [str(y) for y in range(2010, 2015)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "215/55 R16"
            }
        },
        "Golf Mk7": {
            "1.6 TDI / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["105 HP", "110 HP"],
                "years": [str(y) for y in range(2013, 2021)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.4 TSI / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["122 HP", "140 HP", "150 HP"],
                "years": [str(y) for y in range(2013, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            }
        },
        "Golf Mk7.5": {
            "1.0 TSI / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["110 HP"],
                "years": [str(y) for y in range(2017, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            }
        },
        "Polo": {
            "1.4 TDI / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2014, 2018)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/60 R15"
            },
            "1.0 TSI / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["95 HP", "110 HP"],
                "years": [str(y) for y in range(2018, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "Jetta": {
            "1.6 TDI / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["105 HP"],
                "years": [str(y) for y in range(2011, 2019)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.2 TSI / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["105 HP"],
                "years": [str(y) for y in range(2011, 2019)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            }
        }
    },
    "Ford": {
        "Focus": {
            "1.6 TDCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP", "115 HP"],
                "years": [str(y) for y in range(2011, 2019)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.5 TDCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["120 HP"],
                "years": [str(y) for y in range(2015, 2022)],
                "oil": "0W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.0 EcoBoost / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["125 HP"],
                "years": [str(y) for y in range(2015, 2024)],
                "oil": "5W-20",
                "battery": "60 Ah",
                "tire": "205/60 R16"
            }
        },
        "Fiesta": {
            "1.4 TDCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["70 HP"],
                "years": [str(y) for y in range(2008, 2013)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/50 R15"
            },
            "1.5 TDCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP"],
                "years": [str(y) for y in range(2013, 2018)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/50 R15"
            },
            "1.25 / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel"],
                "powers": ["82 HP"],
                "years": [str(y) for y in range(2008, 2018)],
                "oil": "5W-30",
                "battery": "43 Ah",
                "tire": "195/50 R15"
            }
        },
        "Courier": {
            "1.5 TDCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP", "95 HP"],
                "years": [str(y) for y in range(2014, 2024)],
                "oil": "0W-30",
                "battery": "60 Ah",
                "tire": "195/60 R15"
            },
            "1.6 TDCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP"],
                "years": [str(y) for y in range(2014, 2017)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/60 R15"
            }
        },
        "Transit": {
            "2.2 TDCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["100 HP", "125 HP", "155 HP"],
                "years": [str(y) for y in range(2006, 2015)],
                "oil": "5W-30",
                "battery": "75 Ah",
                "tire": "215/75 R16"
            },
            "2.0 EcoBlue / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["130 HP", "170 HP"],
                "years": [str(y) for y in range(2016, 2024)],
                "oil": "0W-30",
                "battery": "80 Ah",
                "tire": "235/65 R16"
            }
        }
    },
    "Toyota": {
        "Corolla": {
            "1.4 D-4D / Dizel (2007-13)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2007, 2014)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.4 D-4D / Dizel (2013-18)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2013, 2019)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.6 Valvematic / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["132 HP"],
                "years": [str(y) for y in range(2013, 2019)],
                "oil": "0W-20",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            },
            "1.5 Vision / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["125 HP"],
                "years": [str(y) for y in range(2019, 2024)],
                "oil": "0W-20",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            },
            "1.8 Hybrid / Hibrit": {
                "fuels": ["Hibrit"],
                "transmissions": ["Otomatik"],
                "powers": ["122 HP", "140 HP"],
                "years": [str(y) for y in range(2019, 2024)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "225/45 R17"
            }
        },
        "Yaris": {
            "1.0 VVT-i / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel"],
                "powers": ["69 HP"],
                "years": [str(y) for y in range(2011, 2021)],
                "oil": "5W-30",
                "battery": "45 Ah",
                "tire": "175/65 R15"
            },
            "1.33 VVT-i / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["99 HP"],
                "years": [str(y) for y in range(2011, 2018)],
                "oil": "5W-30",
                "battery": "50 Ah",
                "tire": "175/65 R15"
            },
            "1.5 Hybrid / Hibrit": {
                "fuels": ["Hibrit"],
                "transmissions": ["Otomatik"],
                "powers": ["100 HP", "116 HP"],
                "years": [str(y) for y in range(2012, 2021)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "175/65 R15"
            }
        },
        "Auris": {
            "1.4 D-4D / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2013, 2019)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.6 Valvematic / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["132 HP"],
                "years": [str(y) for y in range(2013, 2019)],
                "oil": "0W-20",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            }
        }
    },
    "Opel": {
        "Astra": {
            "1.3 CDTI / Dizel (Astra H)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2004, 2014)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.3 CDTI / Dizel (Astra J)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP"],
                "years": [str(y) for y in range(2009, 2016)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "215/50 R17"
            },
            "1.6 / Benzin (Astra J)": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["115 HP"],
                "years": [str(y) for y in range(2009, 2016)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "215/50 R17"
            },
            "1.6 CDTI / Dizel (Astra K)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["136 HP"],
                "years": [str(y) for y in range(2015, 2021)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "225/45 R17"
            },
            "1.4 Turbo / Benzin (Astra K)": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["150 HP"],
                "years": [str(y) for y in range(2015, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "225/45 R17"
            }
        },
        "Corsa": {
            "1.3 CDTI / Dizel (Corsa D)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP", "90 HP"],
                "years": [str(y) for y in range(2006, 2015)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            },
            "1.2 / Benzin (Corsa D)": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel"],
                "powers": ["85 HP"],
                "years": [str(y) for y in range(2006, 2015)],
                "oil": "5W-30",
                "battery": "50 Ah",
                "tire": "185/65 R15"
            },
            "1.4 / Benzin (Corsa E)": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2014, 2020)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "Vectra C": {
            "1.9 CDTI / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["150 HP"],
                "years": [str(y) for y in range(2002, 2009)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "215/55 R16"
            }
        },
        "Insignia": {
            "1.6 CDTI / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["136 HP"],
                "years": [str(y) for y in range(2015, 2021)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "245/45 R18"
            }
        }
    },
    "Hyundai": {
        "i20": {
            "1.4 MPI / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["100 HP"],
                "years": [str(y) for y in range(2014, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/55 R16"
            },
            "1.2 D-CVVT / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel"],
                "powers": ["84 HP"],
                "years": [str(y) for y in range(2014, 2021)],
                "oil": "5W-30",
                "battery": "50 Ah",
                "tire": "185/65 R15"
            },
            "1.4 CRDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2014, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/55 R16"
            }
        },
        "Accent": {
            "1.5 CRDi / Dizel (Accent Era)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["110 HP"],
                "years": [str(y) for y in range(2006, 2013)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R14"
            },
            "1.4 / Benzin (Accent Era)": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["97 HP"],
                "years": [str(y) for y in range(2006, 2013)],
                "oil": "10W-40",
                "battery": "60 Ah",
                "tire": "185/65 R14"
            },
            "1.6 CRDi / Dizel (Accent Blue)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["128 HP", "136 HP"],
                "years": [str(y) for y in range(2011, 2019)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/50 R16"
            }
        },
        "Tucson": {
            "1.6 T-GDI / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["177 HP"],
                "years": [str(y) for y in range(2015, 2021)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "225/60 R17"
            },
            "1.6 CRDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["136 HP"],
                "years": [str(y) for y in range(2018, 2024)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "225/60 R17"
            }
        },
        "Getz": {
            "1.5 CRDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["88 HP", "110 HP"],
                "years": [str(y) for y in range(2002, 2012)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "175/65 R14"
            },
            "1.4 / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["97 HP"],
                "years": [str(y) for y in range(2002, 2012)],
                "oil": "10W-40",
                "battery": "50 Ah",
                "tire": "175/65 R14"
            }
        }
    },
    "Peugeot": {
        "301": {
            "1.6 HDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["92 HP"],
                "years": [str(y) for y in range(2012, 2019)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            },
            "1.5 BlueHDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["100 HP"],
                "years": [str(y) for y in range(2018, 2024)],
                "oil": "0W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "208": {
            "1.4 HDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["68 HP"],
                "years": [str(y) for y in range(2012, 2016)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            },
            "1.2 PureTech / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["82 HP", "100 HP", "110 HP"],
                "years": [str(y) for y in range(2015, 2024)],
                "oil": "0W-30",
                "battery": "60 Ah",
                "tire": "195/55 R16"
            }
        },
        "308": {
            "1.6 e-HDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["115 HP"],
                "years": [str(y) for y in range(2013, 2018)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "205/55 R16"
            },
            "1.2 PureTech / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["130 HP"],
                "years": [str(y) for y in range(2014, 2022)],
                "oil": "0W-30",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            }
        },
        "2008": {
            "1.6 e-HDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["92 HP", "115 HP"],
                "years": [str(y) for y in range(2013, 2020)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "195/60 R16"
            },
            "1.2 PureTech / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["130 HP"],
                "years": [str(y) for y in range(2019, 2024)],
                "oil": "0W-30",
                "battery": "60 Ah",
                "tire": "215/60 R17"
            }
        },
        "3008": {
            "1.6 BlueHDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["120 HP"],
                "years": [str(y) for y in range(2016, 2021)],
                "oil": "0W-30",
                "battery": "72 Ah",
                "tire": "225/55 R18"
            },
            "1.5 BlueHDi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["130 HP"],
                "years": [str(y) for y in range(2018, 2024)],
                "oil": "0W-30",
                "battery": "72 Ah",
                "tire": "225/55 R18"
            }
        }
    },
    "Honda": {
        "Civic": {
            "1.6 i-VTEC / Benzin (FB7)": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["125 HP"],
                "years": [str(y) for y in range(2012, 2017)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "205/55 R16"
            },
            "1.6 i-VTEC / Benzin (FC5)": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Otomatik"],
                "powers": ["125 HP"],
                "years": [str(y) for y in range(2016, 2022)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "215/50 R17"
            },
            "1.5 VTEC Turbo / Benzin (FC5)": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["182 HP"],
                "years": [str(y) for y in range(2017, 2022)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "215/50 R17"
            },
            "1.6 i-DTEC / Dizel (FC5)": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["120 HP"],
                "years": [str(y) for y in range(2018, 2022)],
                "oil": "0W-30",
                "battery": "72 Ah",
                "tire": "215/50 R17"
            },
            "1.5 VTEC / Benzin (FE1)": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Otomatik"],
                "powers": ["129 HP", "182 HP"],
                "years": [str(y) for y in range(2021, 2024)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "215/50 R17"
            }
        },
        "CR-V": {
            "1.6 i-DTEC / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["120 HP", "160 HP"],
                "years": [str(y) for y in range(2013, 2019)],
                "oil": "0W-30",
                "battery": "72 Ah",
                "tire": "225/65 R17"
            },
            "2.0 i-VTEC / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["150 HP"],
                "years": [str(y) for y in range(2007, 2013)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "225/60 R18"
            },
            "1.5 VTEC Turbo / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["193 HP"],
                "years": [str(y) for y in range(2018, 2024)],
                "oil": "0W-20",
                "battery": "60 Ah",
                "tire": "235/60 R18"
            }
        },
        "City": {
            "1.5 i-VTEC / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["121 HP"],
                "years": [str(y) for y in range(2021, 2024)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "185/55 R16"
            }
        },
        "Jazz": {
            "1.3 i-VTEC / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["102 HP"],
                "years": [str(y) for y in range(2015, 2021)],
                "oil": "0W-20",
                "battery": "45 Ah",
                "tire": "185/60 R15"
            }
        }
    },
    "Dacia": {
        "Duster": {
            "1.5 dCi / Dizel (2010-17)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP", "110 HP"],
                "years": [str(y) for y in range(2010, 2018)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "215/65 R16"
            },
            "1.5 Blue dCi / Dizel (2018-23)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["115 HP"],
                "years": [str(y) for y in range(2018, 2024)],
                "oil": "5W-30",
                "battery": "72 Ah",
                "tire": "215/65 R16"
            },
            "1.0 TCe / Benzin": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel"],
                "powers": ["100 HP"],
                "years": [str(y) for y in range(2019, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "215/65 R16"
            },
            "1.3 TCe / Benzin": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["130 HP", "150 HP"],
                "years": [str(y) for y in range(2019, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "215/60 R17"
            }
        },
        "Sandero": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP", "90 HP"],
                "years": [str(y) for y in range(2013, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            },
            "1.5 dCi / Dizel (Stepway)": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP"],
                "years": [str(y) for y in range(2013, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "205/55 R16"
            },
            "1.0 TCe / Benzin": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP", "100 HP"],
                "years": [str(y) for y in range(2021, 2024)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "Logan MCV": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP", "90 HP"],
                "years": [str(y) for y in range(2013, 2021)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "Lodgy": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["90 HP", "110 HP"],
                "years": [str(y) for y in range(2012, 2023)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        },
        "Dokker": {
            "1.5 dCi / Dizel": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["75 HP", "90 HP"],
                "years": [str(y) for y in range(2012, 2022)],
                "oil": "5W-30",
                "battery": "60 Ah",
                "tire": "185/65 R15"
            }
        }
    }
}

def link_vehicle_products(vehicle):
    model_name = vehicle.model_name
    parts = model_name.split(" - ")
    if len(parts) >= 2:
        series = parts[0].strip()
        model_desc = parts[1].strip()
    else:
        series = model_name.strip()
        model_desc = ""
        
    brand = vehicle.brand
    
    oil_spec = None
    battery_spec = None
    tire_spec = None
    
    if brand in CAR_DATA:
        if series in CAR_DATA[brand]:
            matched_data = None
            for key, val in CAR_DATA[brand][series].items():
                if key == model_desc or key in model_desc or model_desc in key:
                    matched_data = val
                    break
            
            if matched_data:
                oil_spec = matched_data.get("oil")
                battery_spec = matched_data.get("battery")
                tire_spec = matched_data.get("tire")
                
    if not (oil_spec or battery_spec or tire_spec) and brand in CAR_DATA:
        for s_name, s_models in CAR_DATA[brand].items():
            for m_name, m_data in s_models.items():
                if m_name in model_name or model_name in m_name:
                    oil_spec = m_data.get("oil")
                    battery_spec = m_data.get("battery")
                    tire_spec = m_data.get("tire")
                    break
            if oil_spec:
                break
                
    if not (oil_spec or battery_spec or tire_spec) and brand in CAR_DATA:
        try:
            first_series = list(CAR_DATA[brand].keys())[0]
            first_model = list(CAR_DATA[brand][first_series].keys())[0]
            m_data = CAR_DATA[brand][first_series][first_model]
            oil_spec = m_data.get("oil")
            battery_spec = m_data.get("battery")
            tire_spec = m_data.get("tire")
        except Exception:
            pass

    from app.models import Product
    all_products = Product.query.all()
    
    vehicle.compatible_products = []
    
    for p in all_products:
        is_compatible = False
        if p.category == 'Motor Yağı' and oil_spec:
            if oil_spec.strip().lower() in p.specs.strip().lower():
                is_compatible = True
        elif p.category == 'Akü' and battery_spec:
            v_num = "".join(filter(str.isdigit, battery_spec))
            p_num = "".join(filter(str.isdigit, p.specs))
            if v_num and p_num and v_num in p_num:
                is_compatible = True
        elif p.category == 'Lastik' and tire_spec:
            if tire_spec.strip().lower() in p.specs.strip().lower():
                is_compatible = True
        elif p.category == 'Jant' and tire_spec:
            for r_size in ["13", "14", "15", "16", "17", "18"]:
                if f"R{r_size}" in tire_spec and r_size in p.specs:
                    is_compatible = True
                    break
                    
        if is_compatible:
            vehicle.compatible_products.append(p)
            
    if len(vehicle.compatible_products) == 0:
        for p in all_products:
            vehicle.compatible_products.append(p)
