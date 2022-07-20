SELECT * FROM pog_godzinowa LIMIT 1000;

SELECT * FROM cva_cases 
INNER JOIN lok_gmin ON 
 substr(cva_cases.teryt_code, 1, 7) = lok_gmin.teryt
INNER JOIN nn_stacje ON lok_gmin.rowid - 1 = nn_stacje.id_gmi 
INNER JOIN stacje ON nn_stacje.id_st1=stacje.id_st 
INNER JOIN pog_dzienna ON stacje.kod_st = pog_dzienna.kod_st 
AND cva_cases.adm_date = substr(pog_dzienna.pog_timestamp, 1, 10);

SELECT COUNT(*) FROM pog_godzinowa;

SELECT * FROM emp_salaries;