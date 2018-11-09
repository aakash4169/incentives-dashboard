
/*program_category,program_type,geographic_focus*/

CREATE TABLE IncentiveProgram (
	program_id int NOT NULL AUTO_INCREMENT,
program_name varchar(200),
program_description varchar(200),
	program_objectives varchar(200),
contact_email varchar(150),
	contact_info varchar(150),
	department varchar(200),
	program_administration_type varchar(100),
	program_cap varchar(100),
	program_finish varchar(50),
	program_start varchar(50),
	program_specifics varchar(4000),
	state varchar(100),
	website varchar(400),	
PRIMARY KEY (program_id)
);

CREATE TABLE BusinessNeeds (
business_needs_id int NOT NULL AUTO_INCREMENT,
business_needs varchar(400) NOT NULL,
PRIMARY KEY (business_needs_id )
);

/*Table that handles the multi valued attribute business_needs*/
CREATE TABLE ProgramBusinessNeeds(
program_id int NOT NULL,
business_needs_id int NOT NULL,
PRIMARY KEY (program_id ,business_needs_id ),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id),
FOREIGN KEY (business_needs_id )REFERENCES BusinessNeeds (business_needs_id)
);

CREATE TABLE Industry(
industry_id int NOT NULL AUTO_INCREMENT,
industry varchar(100) NOT NULL,
PRIMARY KEY (industry_id )
);

/*Table that handles the multi valued attribute industry*/
CREATE TABLE ProgramIndustries(
program_id int NOT NULL,
industry_id int NOT NULL ,
PRIMARY KEY (program_id   ,industry_id   ),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id),
FOREIGN KEY (industry_id  )REFERENCES Industry(industry_id )
);

CREATE TABLE GeographicFocus (
geographic_focus_id int NOT NULL AUTO_INCREMENT,
geographic_focus varchar(100) NOT NULL,
PRIMARY KEY (geographic_focus_id)
);

/*Table that handles the multi valued attribute geographic_focus*/
CREATE TABLE ProgramGeographicFocus(
program_id int NOT NULL,
geographic_focus_id int NOT NULL,
PRIMARY KEY (program_id ,geographic_focus_id ),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id),
FOREIGN KEY (geographic_focus_id )REFERENCES GeographicFocus (geographic_focus_id)
);


CREATE TABLE Category (
category_id int NOT NULL AUTO_INCREMENT,
category varchar(200) NOT NULL,
PRIMARY KEY (category_id)
);

/*Table that handles the multi valued attribute program category*/
CREATE TABLE ProgramProgramCategory(
program_id int NOT NULL,
category_id int NOT NULL,
PRIMARY KEY (program_id ,category_id ),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id),
FOREIGN KEY (category_id )REFERENCES Category (category_id)
);

CREATE TABLE ProgType (
prog_type_id int NOT NULL AUTO_INCREMENT,
prog_type varchar(200) NOT NULL,
PRIMARY KEY (prog_type_id)
);

/*Table that handles the multi valued attribute program_type*/
CREATE TABLE ProgramType(
program_id int NOT NULL,
program_type_id int NOT NULL,
PRIMARY KEY (program_id ,program_type_id ),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id),
FOREIGN KEY (program_type_id )REFERENCES ProgType (prog_type_id)
);
