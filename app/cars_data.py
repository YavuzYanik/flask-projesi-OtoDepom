# Araca özel dinamik özellikler (Marka -> Seri -> Donanım/Model -> Özellikler)
CAR_DATA = {
    "BMW": {
        "3 Serisi": {
            "320d": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["184 HP", "190 HP"],
                "years": [str(y) for y in range(2012, 2025)]
            },
            "320i": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["170 HP"],
                "years": [str(y) for y in range(2012, 2025)]
            }
        },
        "5 Serisi": {
            "520i": {
                "fuels": ["Benzin", "Hibrit"],
                "transmissions": ["Otomatik"],
                "powers": ["170 HP", "205 HP"],
                "years": [str(y) for y in range(2017, 2025)]
            },
            "520d": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["190 HP"],
                "years": [str(y) for y in range(2017, 2024)]
            }
        }
    },
    "Renault": {
        "Clio": {
            "1.0 TCe": {
                "fuels": ["Benzin", "LPG"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP", "100 HP"],
                "years": [str(y) for y in range(2019, 2025)]
            },
            "1.5 dCi": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["90 HP", "110 HP"],
                "years": [str(y) for y in range(2012, 2022)]
            }
        },
        "Megane": {
            "1.3 TCe": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik", "Manuel"],
                "powers": ["140 HP"],
                "years": [str(y) for y in range(2019, 2025)]
            },
            "1.5 Blue dCi": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["115 HP"],
                "years": [str(y) for y in range(2016, 2024)]
            }
        }
    },
    "Toyota": {
        "Corolla": {
            "1.8 Hybrid": {
                "fuels": ["Hibrit"],
                "transmissions": ["Otomatik"],
                "powers": ["122 HP", "140 HP"],
                "years": [str(y) for y in range(2019, 2025)]
            },
            "1.5 Vision": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["125 HP"],
                "years": [str(y) for y in range(2021, 2025)]
            }
        },
        "Yaris": {
            "1.5 Hybrid": {
                "fuels": ["Hibrit"],
                "transmissions": ["Otomatik"],
                "powers": ["116 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            }
        }
    },
    "Ford": {
        "Focus": {
            "1.5 TDCi": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["120 HP"],
                "years": [str(y) for y in range(2015, 2022)]
            },
            "1.0 EcoBoost": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["125 HP"],
                "years": [str(y) for y in range(2012, 2024)]
            }
        },
        "Puma": {
            "1.0 EcoBoost mHEV": {
                "fuels": ["Hibrit", "Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["125 HP", "155 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            }
        }
    },
    "Fiat": {
        "Egea": {
            "1.3 Multijet": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP"],
                "years": [str(y) for y in range(2015, 2025)]
            },
            "1.4 Fire": {
                "fuels": ["Benzin"],
                "transmissions": ["Manuel"],
                "powers": ["95 HP"],
                "years": [str(y) for y in range(2015, 2025)]
            },
            "1.6 Multijet": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["120 HP", "130 HP"],
                "years": [str(y) for y in range(2015, 2025)]
            }
        }
    },
    "Volkswagen": {
        "Golf": {
            "1.0 eTSI": {
                "fuels": ["Hibrit", "Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["110 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            },
            "1.5 eTSI": {
                "fuels": ["Hibrit", "Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["150 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            },
            "1.6 TDI": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["105 HP", "110 HP", "115 HP"],
                "years": [str(y) for y in range(2010, 2020)]
            }
        },
        "Passat": {
            "1.5 TSI": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["150 HP"],
                "years": [str(y) for y in range(2019, 2024)]
            },
            "1.6 TDI": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["120 HP"],
                "years": [str(y) for y in range(2015, 2020)]
            }
        }
    },
    "Honda": {
        "Civic": {
            "1.5 VTEC Turbo": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["182 HP"],
                "years": [str(y) for y in range(2017, 2025)]
            },
            "1.6 i-DTEC": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["120 HP"],
                "years": [str(y) for y in range(2018, 2021)]
            },
            "1.6 Eco": {
                "fuels": ["LPG", "Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["125 HP"],
                "years": [str(y) for y in range(2012, 2022)]
            }
        }
    },
    "Hyundai": {
        "i20": {
            "1.4 MPI": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik", "Manuel"],
                "powers": ["100 HP"],
                "years": [str(y) for y in range(2015, 2025)]
            },
            "1.0 T-GDI": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["100 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            }
        },
        "Tucson": {
            "1.6 T-GDI": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["150 HP", "180 HP"],
                "years": [str(y) for y in range(2021, 2025)]
            },
            "1.6 CRDi": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["136 HP"],
                "years": [str(y) for y in range(2019, 2025)]
            }
        }
    },
    "Mercedes-Benz": {
        "C-Serisi": {
            "C 200": {
                "fuels": ["Benzin", "Hibrit"],
                "transmissions": ["Otomatik"],
                "powers": ["184 HP", "204 HP"],
                "years": [str(y) for y in range(2015, 2025)]
            },
            "C 200 d": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["136 HP", "160 HP"],
                "years": [str(y) for y in range(2015, 2022)]
            }
        },
        "E-Serisi": {
            "E 200 d": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["160 HP"],
                "years": [str(y) for y in range(2017, 2024)]
            }
        }
    },
    "Audi": {
        "A3": {
            "1.5 TFSI": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["150 HP"],
                "years": [str(y) for y in range(2018, 2025)]
            },
            "1.6 TDI": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["110 HP", "116 HP"],
                "years": [str(y) for y in range(2014, 2020)]
            }
        },
        "A4": {
            "2.0 TDI": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["190 HP"],
                "years": [str(y) for y in range(2016, 2025)]
            }
        }
    },
    "Peugeot": {
        "208": {
            "1.2 PureTech": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik", "Manuel"],
                "powers": ["75 HP", "100 HP", "130 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            },
            "1.5 BlueHDi": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["130 HP"],
                "years": [str(y) for y in range(2020, 2024)]
            }
        },
        "3008": {
            "1.5 BlueHDi": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["130 HP"],
                "years": [str(y) for y in range(2018, 2025)]
            }
        }
    },
    "Skoda": {
        "Octavia": {
            "1.0 e-TEC": {
                "fuels": ["Hibrit", "Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["110 HP"],
                "years": [str(y) for y in range(2021, 2025)]
            },
            "1.5 TSI": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik"],
                "powers": ["150 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            },
            "1.6 TDI": {
                "fuels": ["Dizel"],
                "transmissions": ["Otomatik"],
                "powers": ["115 HP"],
                "years": [str(y) for y in range(2014, 2020)]
            }
        }
    },
    "Dacia": {
        "Duster": {
            "1.3 TCe": {
                "fuels": ["Benzin"],
                "transmissions": ["Otomatik", "Manuel"],
                "powers": ["130 HP", "150 HP"],
                "years": [str(y) for y in range(2019, 2025)]
            },
            "1.5 Blue dCi": {
                "fuels": ["Dizel"],
                "transmissions": ["Manuel", "Otomatik"],
                "powers": ["115 HP"],
                "years": [str(y) for y in range(2018, 2025)]
            },
            "1.0 ECO-G": {
                "fuels": ["LPG"],
                "transmissions": ["Manuel"],
                "powers": ["100 HP"],
                "years": [str(y) for y in range(2020, 2025)]
            }
        }
    }
}
