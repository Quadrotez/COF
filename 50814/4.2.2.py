def assess_collapse(mass, astral_body='Earth', CRITICAL=1000):
	GRAVITY = {
    "Earth": 9.8,
    "Jupiter": 24.79,
    "Moon": 1.63,
	}


	return (mass*GRAVITY[astral_body])>=CRITICAL