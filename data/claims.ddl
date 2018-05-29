drop table if exists claims;

create table claims (
rx_number varchar(255) not null,
member_group varchar(255),
drug_ndc varchar(255),
rx_count varchar(255),
process_date varchar(255),
new_refill_indicator varchar(255),
brand_generic_ind varchar(255),
mail_order_ind varchar(255),
lob_code varchar(255),
lob_desc varchar(255),
pa_indicator varchar(255),
benefit_plan_code varchar(255),
business_unit_id varchar(255),
paid_amount float,
ingredient_cost float,
sales_tax float,
copay_amount float
);

load data infile '/data/claims.csv' into table claims
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;
