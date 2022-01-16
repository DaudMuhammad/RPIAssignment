alter table movies add column if not exists lexemestitle tsvector;
update  movies set lexemestitle = to_tsvector(title);
update movies set rank = ts_rank(lexemestitle, plainto_tsquery(
(
select title from movies where url='another-earth'
)
));
drop table IF EXISTS recommendationsbasedonsummaryfield;
CREATE table recommendationsbasedonsummaryfield as select url,rank from movies where rank > -1 order by rank desc limit 50;
\copy ( select * from recommendationsbasedonsummaryfield) to '/home/pi/RSL/top50reco_title(Another Earth).csv' with csv;
