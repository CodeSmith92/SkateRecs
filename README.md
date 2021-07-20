# SkateRecs

## Intro
For most (men's) hockey skates, a person's skate size corresponds to a size of 1.5 less than their shoe size (think dress shoe). This program returns skate size, and recommends Bauer and CCM skate models/fit profiles based on foot width (and foot length/width ratio). 


## Setup

1. Install dependencies:

        
        pip install pandas
        
        
2. Clone repository:

        git clone https://github.com/CodeSmith92/SkateRecs.git


## CLI

When running from the command line, parameters should be passed as key-value pairs. For example:

    python skates.py --shoe_size <shoe size> --foot_width <width-cm> --foot_length <length-cm> 



| Key   | Type | Options | Required | Description|
| ----- | ---- | --------| -------- | ---------- |
| `shoe_size`  | float  | 6.0-12.0| Yes     | Size corresponds to US M. Values are inclusive. Increments of 0.5.  |
| `foot_width` | float |         | Yes     |      units: cm      |
| `foot_length`  | float  |         | No    |   If no input, default value is assigned in cm based on shoe_size.         |


Example:

    python skates.py --shoe_size 10.5 --foot_width 10.16 
    
