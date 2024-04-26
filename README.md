<h1> Video Overview </h1>

[![TextDNA](https://img.youtube.com/vi/6U1lD_LM_7o/0.jpg)](https://www.youtube.com/watch?v=6U1lD_LM_7o)

### Table of Contents 
* [Project Overview](#project-overview)
* [Demo](#demo)
* [Features](#features)
* [Documentation](#documentation)
* [Key Algorithm](#key-algorithm)
* [Application Layers and Key Classes](#application-layers-and-key-classes)
* [System Requirements](#system-requirements)
* [Installation Guide](#installation-guide)
* [Setup](#setup)
* [Deployment Guidelines](#deployment-guideline)
* [Changelog](#changelog)



### Project Overview

The aim of the project was to develop a web interface that allows academics to determine the authenticity of students submissions. The project was developed for our client Eduardo Oliveira, a faculty member at the University of Melbourne who requested an interface to utilize the stylometry algorithm they had developed. 

### Demo

The hosted website can be found at https://textdna.azurewebsites.net/
<p align ="center">
    <img src="images\front-page.jpg" width="600">
</p>

It is not currently up as deploying on Azure comes with costs and as such the client has informed us to avoid deploying it unless necessary

Demonstration Video: https://youtu.be/6U1lD_LM_7o

### Features

* Sprint 1
    * Develop a profile for a student to be used for analysis
    * Manage Class  

* Sprint 2
    * Add and View Student Profiles to the Class
    * Add and View Class Assignments to Class
    * View Assignment Submissions 
    * Create an account 
    * Log in and out of the interface

* Sprint 3
    * Upload Submissions
    * Analyze text against a profile that is stored
        *  View Analysis Score 
        *  View Submitted Document




### Documentation

The key documentation regarding the project such as User Stories, Requirements, User Personas and Motivational Model can all be found in the [documentation](docs) folder. 

The test cases utilized when verifying the functionality can be found in the [tests](tests) folder 

### Key Algorithm
Each trained profile requires 4  items to be created: 
Word2Vec model
Previous essays turned to vectors by Word2Vec model
clf_network model [tensorflow]
base_network model [tensorflow]

The algorithm steps can be observed in "root\backend\algorithm_scripts\algorithm.py" 
Note: The file paths for the parametres of the trained models are supplied as parametres:

1. Converts unknown text into vectors using trained Word2Vec model
2. Extract text features using base_network model
3. Using clf_network model, Compares the text features to the trained profile's text features, and outputs a similarity score

In our project, we have decided to create one trained profile only (for simplicity), so every submission (regardless of the student) is compared against that same trained model, rather than a different trained model for each student.

To train new models for new profiles, store trained models and pass their filepaths to the function in "root\backend\algorithm_scripts\algorithm.py". 

To generate / train models, refer to the client's [Eduardo] python notebook in:
https://unimelbcloud-my.sharepoint.com/personal/eduardo_oliveira_unimelb_edu_au/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Feduardo_oliveira_unimelb_edu_au%2FDocuments%2F2023%2FProject_Code-20230815T025227Z%2FProject_Code%2FPAN14_Code 


### Application Layers and Key Classes

#### Application Layers
<p align ="center">
    <img src="docs\Architectural Diagram.jpg" width="600">
</p>

#### Key Application Classes and Pages
The key application pages and their connections can be seen below 
<p align ="center">
    <img src="images\application_pages.jpg" width="600">
</p>

To view appliation design and layout in more detail you can access the Figma
* [Low Fidelity Prototype](https://www.figma.com/file/qmZvg96JrZJDOzqwITEPKl/Low-Fidelity-Protoype?type=design&node-id=0%3A1&mode=design&t=1DJqkPlTPLxTafgt-1)
* [High Fideltiy Protoype](https://www.figma.com/file/DWnINDGCW5ZfZITFtEow0p/High-Fidelity-Protoype?type=design&node-id=0%3A1&mode=design&t=9QwltwLYuzZ6Wo1A-1)

### System Requirements

* Tools
    * Front End Tools:
        * REACT : Used to design the web interface
        * HTML : Used to design the web interface
        * SCSS: Used to streamline the process of utilizing CSS for the website
    * Back End Tools:
        * Python: Used to develop our backend scripts to allow dynamic content on the webpages
        * Powershell: Used to create communication with the data storage and database hosted on Azure
    * Database and Server Tools:
        * Microsoft Azure: Used to deploy our interface
        * SQL : Used to query information stored within the database
* Databases
    * Entity- Relationship Diagram: 
    <p align ="center">
        <img src="docs\Database_Structure\Entity_Relationship_Diagram.png" width="600">
    </p>
    * Phyical Database Diagram
    <p align ="center">
        <img src="docs\Database_Structure\Physical_Database_Diagram.png" width="600">
    </p>

* Relevant dependencies and their versions can be found at [requirements.txt](requirements.txt)

### Installation Guide 
* Install dependencies: 
    * Backend:
        * Ensure you have python and pip installed 
        * "pip install -r requirements.txt" [Found in COMP30022 directory]
        * curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.10.5.1-1_amd64.apk
        * curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.10.1.1-1_amd64.apk
        * sudo apk add --allow-untrusted msodbcsql17_17.10.5.1-1_amd64.apk
        * sudo apk add --allow-untrusted mssql-tools_17.10.1.1-1_amd64.apk
        * Download Powershell 7 and run Install-Module-name Az
    * Frontend: 
        1. Ensure you have NodeJS installed
        2. cd "COMP30022\root\frontend"
        3. npm install react-scripts --save
        4. npm install --save @fortawesome/free-solid-svg-icons
        5. npm install --save @fortawesome/react-fontawesome
* Log into https://portal.azure.com/ using credentials and go into sql server instance "sql-server-capstone-project" and add your IP address into firewall settings under "networking"


Credentials to access repository , storage account, server , databases
The interface uses the following services which can be accessed through https://portal.azure.com/:
* storage account [storage1itproject]
* SQL Database [sql-db-capstone-project]
* SQL Server [sql-server-capstone-project]
* Virtual Machine [VM-capstone-project] (to host the back-end in deployment)
* App service [textDNA] (for front-end and other credentials for back-end)

__Credentials are:__
* Username: Shaun@younismamoun2001gmail.onmicrosoft.com
* Password: Mosa2012351

### Setup
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/shaunchowGO/COMP30022.git

2. Open 2 terminals, one to run front-end, and another to run back-end

3. Install dependencies and follow instructions in [Installation Guide](#installation-guide)

4. **Backend Setup:**

   ```bash
    cd root/backend
    pip install -r requirements.txt
    python app.py
5. **Frontend Setup:**

    ```bash
    cd root/frontend
    npm install
    npm install
    npm start

This should automatically open a new tab your localhost path, where you can interact  with the interface.

### Deployment Guideline:
    * Log into https://portal.azure.com/:
    * Open CLI in the cloud (Bash terminal hosted on Azure)
    * Go into textDNA appService
    * Navigate to the git repo [already cloned]
    * Run front-end by:
        * Start the instance of textDNA app
        * cd "COMP30022\root\frontend"
        * az webapp up [run this command  in frontend directory]
    * Run back-end by:
        * edit the link in file ...
        * navigate to [VM-capstone-project]  instance
    * Start it
        * Open CLI and run:
        * "az ssh vm --resource-group rg-capstone-project --vm-name VM-capstone-project --subscription 05dcda3f-04cb-4057-bfbe-472610744c79"
        * cd COMP30022
        * pip install -r requirements.txt
        * cd root\backend
        * python3 app.py
        * Go to website "textdna.azurewebsites.net"

### Changelog 

Format: Change_ID[User_Story_ID,User_Story_ID...]

#### Sprint 1
This sprint focused on creating  the foundations of our project. The aim was to establish a simple working interface 

Changes: 
* 1.0.8: Added Initial requirements for dependencies
* 1.0.7[2.3]: Added table creation code with description
* 1.0.6[2.3]: Initial backend connection
* 1.0.5[2.3]: Worked on file structure
* 1.0.4[2.3]: Get student & teacher
* 1.0.3[1.1,1.2]: added nav, landing and allow for page nav
* 1.0.2[2.3]: Added teacher & group profiles
* 1.0.1[2.3,1.3]: Added file structure & studentProfile


#### Sprint 2
This sprint was to resolve issues discovered in v1.0. We continued development and added additional features and refined product. The aim was also to connect required services such as databases to the interface 

Changes: 
* 2.0.15[1,2]: Updated table creation code.txt
* 2.0.14[1,2]: Added Line to run SQL from PowerShell
* 2.0.13[1,2]: Create API connection
* 2.0.12[1,2]: Changing file structure
* 2.0.11[1.1]: Add files via upload
* 2.0.10[1.1,1.2]: Added images and assets to landing page
* 2.0.9[1.1,2.3,2.2]: Updated profile UI, added ui for adding new items and files
* 2.0.8[1.1,1.2]: Stylised login and sign-up page
* 2.0.7[1,2]: Add or update the Azure App Service build and deployment workflow config
* 2.0.6[2.1,2.2]: Updated main landing to match figma
* 2.0.5[2.1,2.2]: Added styling to landing page
* 2.0.4[2.3.1,2.3.3]: Updated profile and added assignments page
* 2.0.3[1.2,2.3]: Added styling to profile pages and assignment page
* 2.0.2[2.1,2.2]: Created prototype for landing page
* 2.0.1[1.1]: Added FileUpload component
* 2.0.0[2.1,2.2]: Added signup/login page and footer

#### Sprint 3
This sprint was to complete the development of all requried functionalities. Focused on preparing the product to be prepared for handover to client. Preparation for deployment was also a focus of the Sprint 

Changes:
* 3.0.32[2.3]: Added group profile & academicCohort Query
* 3.0.31[2.3]: Added New teacher page query
* 3.0.30[1.2]: Added hashing
* 3.0.29[1.1]: added sign up
* 3.0.28[1.2]: added login, replaced title and favicon
* 3.0.27[1.3,1.3.1]: Uploaded algorithm files
* 3.0.26[2.3.1]: Added student assignment info
* 3.0.25[2.3.2]: Added subject page data
* 3.0.24[1.2]: Can switch academic profile
* 3.0.23[1.2,2.3.1]: Added loading icon to student and centered it, make student profile dynamic'
* 3.0.22[1,2]: Make teacher page dynamic data
* 3.0.21[1,2]: Update Submissions_for_assignment.sql
* 3.0.20[1,2]: Update Subject_Page_query.sql
* 3.0.19[1,2]: Submitting required queries for dynamic page
* 3.0.18[2.3.1]: Updated frontend, make frontend more responsive, added student cards
* 3.0.17[1.1,1.2]: Overhauled landing page
* 3.0.16[1,2]: Uploading latest scripts
* 3.0.15[1,2]: Update run_ps_script.py
* 3.0.14[1,2]: SQL Insertion APIs
* 3.0.13[1,2]: fixed padding issue in filter
* 3.0.12[1,2]: Created Back-end automated testing
* 3.0.11[1,2]: Change dashboard to filter
* 3.0.10[1,2]: Update requirements.txt
* 3.0.9[1.1]: Limit import to only pdf, cleaned up design
* 3.0.8[1.2,2.3.1,1.3]: added dropdown list in login, added view students in group page, fixed popup bug, updated landing page, add ui to compare students with file
* 3.0.7[1,2]: Created python SQL connection
* 3.0.6[1,2]: Add or update the Azure App Service build and deployment workflow config
* 3.0.5[1,2]: Initial setting up of routes
* 3.0.4[1,2]: Added run_ps_script.py
* 3.0.3[1.1]: Add files via upload
* 3.0.2[1,2]: Cleaned up code, prevent scrolling on popup, fixed visual bug
* 3.0.1[1,2]: Small edits to running powershell on python
* 3.0.0[1,2]: Added Output of Query in Python Dict

#### Sprint 4
This sprint was to test the current capabilities of the interface. We aimed to debug issues within the interface and continue to refine the interface 

Changes: 
* 4.0.11[2.3.1]: fixed student profile view
* 4.0.10[2.3]: remove delete buttons
* 4.0.9[1.1]: Ensured upload functionality working
* 4.0.7[1.3.2]: Added view document
* 4.0.6[2.3]: subject name
* 4.0.5[1.2,1.3]: student id & name fix
* 4.0.4[2.3.1]: make view student dynamic
* 4.0.3[2.3.1]: make student card dynamic
* 4.0.2[1.1]: readded dropdown in import
* 4.0.1[1.1]: upload button
* 4.0.0[2]: Removed subject from navbar
