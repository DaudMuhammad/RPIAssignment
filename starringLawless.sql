alter table movies add column if not exists lexemesStarring tsvector;
update  movies set lexemesStarring = to_tsvector(Starring);
update movies set rank = ts_rank(lexemesStarring, plainto_tsquery(
(
select Starring from movies where url='lawless'
)
));
drop table IF EXISTS recommendationsbasedonsummaryfield;
CREATE table recommendationsbasedonsummaryfield as select url,rank from movies where rank > -1 order by rank desc limit 50;
\copy ( select * from recommendationsbasedonsummaryfield) to '/home/pi/RSL/top50reco_starringLawless.csv' with csv;
