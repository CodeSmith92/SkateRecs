# SkateRecs

## Intro
For most (men's) hockey skates, a person's skate size corresponds to a size of 1.5 less than their shoe size (think dress shoe). This program returns the user's likely skate size, and will recommend Bauer and CCM skate models/fit profiles based on the user's foot length-to-width ratio. The foot_length argument is optional; if not passed, the program will estimate foot_length based on user input for shoe_size. 


## Setup

1. Install dependencies:

        
        pip install pandas
        
        
2. Clone repository:

        git clone https://github.com/CodeSmith92/SkateRecs.git


## CLI

When running from the command line, terminal, or shell, parameters must be passed as key-value pairs. For example:

    python skates.py --shoe_size <shoe size> --foot_width <width-cm> --foot_length <length-cm> 



| Key   | Type | Options | Required | Description|
| ----- | ---- | --------| -------- | ---------- |
| `shoe_size`  | float  | 6-13| Yes     | Size corresponds to US M. Values are inclusive. Increments of 0.5.  |
| `foot_width` | float |         | Yes     |      units: cm      |
| `foot_length`  | float  |         | No    |   If no input, default value is assigned in cm based on shoe_size.         |


Example:

    python skates.py --shoe_size 10.5 --foot_width 10.16 
    
## Planned updates
- [ ] Incorporate instep, forefoot, ankle, and heel profiles
- [ ] Implement "experience" argument where choices=['beginner', 'intermediate', 'advanced'] and specific skate model suggestions will be made based on user input. 

## Webpage sources
1. [Foot length estimates and width ratio cutoffs](https://www.inlinewarehouse.com/lc/icehockeyskatesizing.Html)
2. [Choosing the right hockey skates](https://puckstop.com/blog/how-to-choose-the-right-ice-hockey-skates-find-the-ultimate-fit)
3. [CCM vs Bauer](https://goingbardown.com/ccm-vs-bauer-hockey-skates/)
4. [Vapor vs Supreme vs Nexus I](https://www.purehockey.com/c/bauer-supreme-vs-vapor-vs-nexus-skates)
5. [Vapor vs Supreme vs Nexus II](https://discounthockey.com/blogs/news/81929475-bauer-vapor-supreme-nexus-which-one-is-right-for-me)
6. [Ribcor vs Jetspeed vs Tacks I](https://www.purehockey.com/c/ccm-jetspeed-vs-ribcor-vs-tacks-hockey-skates)
7. [Ribcor vs Jetspeed vs Tacks II](https://discounthockey.com/blogs/news/93726659-ccm-jetspeed-tacks-ribcor-which-one-is-right-for-me)
8. [Skate lineups and models by release year](https://beerleaguetips.com/article/hockey-skate-lineup-comparison/)

## Video sources
1. [5 things all hockey players should know before buying skates](https://www.youtube.com/watch?v=ke_mHR_59cY&list=PLFVG1Wz0eNjhJVhA9_DJ3fJaBRDmMIu8q&index=4)
2. [CCM Tacks, RBZ, Ribcor (2014)](https://www.youtube.com/watch?v=7fvRSc44uGM&list=PLFVG1Wz0eNjhJVhA9_DJ3fJaBRDmMIu8q&index=1)
3. [CCM Tacks, JetSpeed, Ribcor (2016)](https://www.youtube.com/watch?v=yXK61_E6Klg&list=PLFVG1Wz0eNjhJVhA9_DJ3fJaBRDmMIu8q&index=2)
4. [CCM Tacks, JetSpeed, Ribcor (2018)](https://www.youtube.com/watch?v=C5zIHbgSqzk&list=PLFVG1Wz0eNjhJVhA9_DJ3fJaBRDmMIu8q&index=3)
5. [CCM Tacks, JetSpeed, Ribcor (2019)](https://www.youtube.com/watch?v=tAjN296MQyU)
6. [Bauer Nexus, Supreme, Vapor (2013)](https://www.youtube.com/watch?v=-LqCSvEqTSo)
7. [Bauer Nexus, Supreme, Vapor (2016)](https://www.youtube.com/watch?v=1eR0-kJa8eY&list=PLFVG1Wz0eNjhJVhA9_DJ3fJaBRDmMIu8q&index=6)
8. [Bauer Nexus, Supreme, Vapor (2017)](https://www.youtube.com/watch?v=ct_z_7Wpxeo)
9. [Bauer Nexus, Supreme, Vapor (2018)](https://www.youtube.com/watch?v=XLxiir_Pwm4)
10. [Bauer Nexus, Supreme, Vapor (2019)](https://www.youtube.com/watch?v=aIcazwpuUD0)
11. [Bauer 2020 performance fit system](https://www.youtube.com/watch?v=kvSyoc5ANBM)
13. [CCM 2021 skate fit profiles](https://www.youtube.com/watch?v=xnutF6IiQiQ&t=546s)
14. [CCM 2021 skate fit profiles II](https://www.youtube.com/watch?v=CXuQRJaRbaw&list=PLFVG1Wz0eNjhJVhA9_DJ3fJaBRDmMIu8q&index=5)

