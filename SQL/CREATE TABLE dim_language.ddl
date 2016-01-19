CREATE TABLE `eval` (
  `id`  INTEGER PRIMARY KEY AUTOINCREMENT,
  `project_name`  TEXT,
  `evaluator_first_name`  TEXT,
  `evaluator_last_name` TEXT,
  `evaluator_role`  TEXT,
  `evaluee_first_name`  TEXT,
  `evaluee_last_name` TEXT,
  `evaluee_role`  TEXT,
  `comments`  TEXT,
  `rating`  TEXT
);

CREATE TABLE projects (
id integer PRIMARY KEY AUTOINCREMENT
, company text
, contact_first_name text
, contact_last_name text
, project_name text
, project_skills text
, project_summary text
, due_date date
, team_size integer
);


CREATE TABLE dim_language
(
  language_key integer NOT NULL,
  language text,
  CONSTRAINT dim_language_pkey PRIMARY KEY (language_key)
);



CREATE TABLE dim_project
(
  project_key integer NOT NULL,
  project_id integer,
  project_name text,
  skills_needed text,
  project_start_date date,
  project_end_date date,
  project_contact text,
  approx_time_needed_in_number_of_weeks integer,
  urgency boolean,
  CONSTRAINT dim_project_pkey PRIMARY KEY (project_key)
);

CREATE TABLE dim_project_type_skill
(
  project_type_skill_detail integer,
  project_type text,
  skill_key integer
);

CREATE TABLE dim_role
(
  role_key integer NOT NULL,
  role text
);


CREATE TABLE dim_skill
(
  skill_key integer NOT NULL,
  skill text,
  CONSTRAINT dim_skill_pkey PRIMARY KEY (skill_key)
);



CREATE TABLE dim_swb_comments
(
  comment_key integer,
  evaluator_id integer,
  evaluator_first_name text,
  evaluator_last_name text,
  evaluator_email text,
  evaluated_first_name text,
  evaluated_last_name text,
  evaluated_email text,
  project_id integer,
  project_name text,
  comments text,
  rating integer,
  would_recommend boolean
);


CREATE TABLE dim_swb_committee
(
  swb_committee_key integer,
  member_first_name text,
  member_last_name text,
  member_email text,
  member_position text,
  position_effective_at date,
  position_term_at date
);


CREATE TABLE dim_swb_coordinators
(
  swb_coordinator_key integer,
  coordinator_first_name text,
  coordinator_last_name text,
  coordinator_email text,
  last_project_id integer,
  is_current_on_project boolean,
  coordinator_effective_date date,
  coordinator_term_date date
);



CREATE TABLE dim_volunteer
(
  volunteer_key integer NOT NULL,
  first_name text,
  last_name text,
  phone_number text,
  email text,
  country text,
  timezone text,
  state text,
  current_position text,
  signed_up_date timestamp without time zone,
  last_update_date timestamp without time zone,
  active_for_volunteering boolean,
  volunteer_id integer,
  last_project_id integer,
  current_employer text,
  is_currently_on_project boolean,
  CONSTRAINT dim_volunteer_pkey PRIMARY KEY (volunteer_key)
);



CREATE TABLE dim_volunteer_language_detail
(
  volunteer_language_detail_key integer,
  volunteer_key integer,
  language_key integer
);


CREATE TABLE dim_volunteer_role_detail
(
  volunteer_role_detail_key integer,
  volunteer_key integer,
  project_key integer,
  role_key integer
);


CREATE TABLE dim_volunteer_skill_detail
(
  volunteer_skill_detail_key integer,
  volunteer_key integer,
  skill_key integer
);



CREATE TABLE fact_project_volunteer
(
  project_volunteer_key integer NOT NULL,
  project_id integer,
  volunteer_id integer,
  project_type text,
  project_contact text,
  project_swb_coordinator text,
  project_lead text,
  volunteer_name text,
  volunteer_email text,
  volunteer_role text,
  project_name text,
  project_term_date date,
  project_effective_date date,
  CONSTRAINT dim_project_volunteer_pkey PRIMARY KEY (project_volunteer_key)
);
