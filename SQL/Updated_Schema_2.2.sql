/*Create Table Scripts*/

CREATE TABLE IncentiveProgram (
	program_id int NOT NULL AUTO_INCREMENT,
	program_name varchar(200),
	program_description text,
	program_objectives text,
	contact_email varchar(75),
	contact_info varchar(66),
	department varchar(200),
	program_administration_type enum('Statutory', 'Discretionary'),
	program_cap varchar(100),
	program_finish varchar(20),
	program_start varchar(20),
	program_specifics text,
	state varchar(50),
	website varchar(200),
PRIMARY KEY (program_id)
);

/*Table that handles the multi valued attribute business_needs*/
CREATE TABLE ProgramBusinessNeeds(
program_id int NOT NULL,
business_needs ENUM(
'Tax/Regulatory burden reduction',
'Facility/site location',
'Business management',
'Marketing & sales assistance',
'Professional networking',
'Tech & product development',
'Other',
'Product & process improvement',
'Workforce prep or development',
'Capital access or formation',
'Infrastructure Improvement') NOT NULL,
PRIMARY KEY (program_id, business_needs ),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id)
);

/*Table that handles the multi valued attribute industry*/
CREATE TABLE ProgramIndustry(
program_id int NOT NULL,
industry ENUM( 
'Manufacturing',
'Transportation and Warehousing',
'Mining, Quarrying, and Oil and Gas Extraction',
'Professional, Scientific, and Technical Services',
'Management of Companies and Enterprises',
'Arts, Entertainment, and Recreation',
'Accommodation and Food Services',
'Agriculture, Forestry, Fishing and Hunting',
'Construction',
'Wholesale Trade',
'Information',
'Utilities',
'Finance and Insurance',
'Health Care and Social Assistance',
'Public Administration',
'Educational Services',
'Administrative and Support and Waste Management and Remediation Services',
'Other Services (except Public Administration)',
'Real Estate and Rental and Leasing',
'Retail Trade') NOT NULL,
PRIMARY KEY (program_id, industry ),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id)
);

/* Table that handles the multi valued attribute Geographic Focus */
CREATE TABLE ProgramGeographicFocus(
program_id int NOT NULL,
geographic_focus ENUM( 
'Development/redevelopment zone',
'Specific region/district',
'Statewide',
'Rural community') NOT NULL,
PRIMARY KEY (program_id,geographic_focus),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id)
);

/* Table that handles the multi valued attribute Program Category */
CREATE TABLE ProgramCategory(
program_id int NOT NULL,
program_category ENUM(
'Direct Community Financing',
'Tax',
'Indirect Business Financing',
'Other',
'Direct Business Financing') NOT NULL,
PRIMARY KEY (program_id,program_category),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id)
);

/* Table that handles the multi valued attribute Program Type */
CREATE TABLE ProgramType(
program_id int NOT NULL,
program_type ENUM(
'Tax deferral',
'Tax credit',
'Tax refund or rebate',
'Equity investment',
'Grant',
'Tax exemption',
'Loan/Loan Participation',
'Loan guarantee',
'Preferential rate',
'Other',
'Tax abatement',
'Collateral Support',
'Tax deduction',
'Insurance') NOT NULL,
PRIMARY KEY (program_id,program_type),
FOREIGN KEY (program_id) REFERENCES IncentiveProgram(program_id)
);

CREATE TABLE Deal(
	deal_id int NOT NULL AUTO_INCREMENT,
	company_name varchar(100),
	contact_name varchar(100),
	contact_position varchar(100),
	contact_email varchar(75),
	contact_phone varchar(10),
	new_jobs int,
	safe_jobs int,
	capEx int,
	incentive int,
	deal_date date,
PRIMARY KEY (deal_id)
);

/* Table that handles cross-reference from Program to Deal */
CREATE TABLE DealProgram(
	deal_id int NOT NULL,
	program_id int NOT NULL,
	PRIMARY KEY (deal_id, program_id),
	FOREIGN KEY (deal_id) REFERENCES Deal (deal_id),
	FOREIGN KEY (program_id) REFERENCES IncentiveProgram (program_id)
);




