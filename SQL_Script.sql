
/* 

The number of tables 
*/
select count(*) from information_schema.tables where table_schema = 'public';

--==============================================================================================================================================================================================


/* 

The number of records in each of the tables given in the MIT section

*/
SELECT COUNT(*) FROM mdl_logstore_standard_log ;
SELECT COUNT(*) FROM mdl_context ;
SELECT COUNT(*) FROM mdl_user ;
SELECT COUNT(*) FROM mdl_course ;
SELECT COUNT(*) FROM mdl_modules  ;
SELECT COUNT(*) FROM mdl_course_modules ;
SELECT COUNT(*) FROM mdl_course_modules_completion  ;
SELECT COUNT(*) FROM mdl_grade_grades  ;

--==============================================================================================================================================================================================


/* 

Number of quiz submissions by hour of day

*/
select count(id), EXTRACT(HOUR FROM to_timestamp(timecreated))from mdl_logstore_standard_log where action='submitted' AND component='mod_quiz' group by EXTRACT(HOUR FROM to_timestamp(timecreated));

--==============================================================================================================================================================================================


/* 

Count of log events per user for the following verbs

*/
SELECT action, count(action) AS Count FROM mdl_logstore_standard_log GROUP BY action ORDER BY count DESC ;

--==============================================================================================================================================================================================


/* 



