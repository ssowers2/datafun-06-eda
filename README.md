# datafun-06-eda

### Purpose  
This project analyzes historical suicide rates in the United States to identify the demographic groups most at risk. It examines trends over time, age groups most affected, differences by sex and race, and any high risk populations.

## Step 1: New Project Setup
1. Initialize Repository: Create a new GitHub repository named **datafun-05-sql** with a default `README.md`.
2. Clone the repository to your local machine in the **Projects** folder.
3. Open the project folder in **VS Code**.

## Step 2: Add Essential Files
1. **.gitignore**  
   Add a `.gitignore` file to specify files and folders to exclude from version control. You can reference an existing `.gitignore` template for Python projects.
2. **requirements.txt**  
   This file lists all necessary packages for the project. Review and adjust it to include or exclude packages based on your project’s needs.
3. **README.md**  
   Edit README.md to record commands, process, and notes so far as the project progresses.
4. 5. This is good time to `git add .`, `git commit -m "Message"`, `git push -u origin main` files to GitHub

## Step 3: Create and Manage Virtual Environment
1. Run command `git pull` first, to make sure the current project contents are on the machine.
2. Windows PowerShell: `python -m venv .venv` to create a new .venv environment in the project repo.
3. Activate the Virtual Environment: `.\.venv\Scripts\activate`

## Step 4: Install Required Packages
`pip install -r requirements.txt` to install all packages at once OR use `py -m pip install` commands to add packages on the go (e.g. `py -m pip install pandas` or group installs `pip install numpy pandas matplotlib seaborn`)

## Step 5: Select Python Interpreter in VS Code
1. Ensure VS Code is set to use the .venv environment.
2. Open the command palette using (Windows) Ctrl + Shift + P.
3. Type "Python: Select Interpreter".
4. Choose the interpreter inside the .venv folder located in the project root directory.
5. This is good time to `git add .`, `git commit -m "Message"`, `git push -u origin main` files to GitHub

## Step 6: Select a dataset, provide a link and its description, and possible areas to analyze
1. Data Source: https://data.gov 
2. Dataset: https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1
3. Description: This dataset provides historical suicide death rates in the United States, categorized by age, sex, race, and Hispanic origin. The data spans multiple years and includes estimated suicide rates per 100,000 residents, adjusted for age.
4. Trends Over Time: Analyze how suicide rates have changed across decades
5. Demographic Disparities: Compare rates across different races, sexes, and age groups.
6. Age-Specific Trends: Identify the most vulnerable age groups.
7. Gender Differences: Examine male vs. female suicide rates. 
8. Race and Ethnicity Impact: Investigate whether certain racial or ethnic groups have higher risk factors.

## Project Structure

## Git Commands Reminders 
1. Add Changes: `git add .`
2. Commit Changes: 5. `git commit -m "Message"`
3. Push Changes to GitHub: `git commit -m "Message"`
4. Pull Latest Changes:  `git push -u origin main`