alter table movies add column if not exists lexemesSummary tsvector;
update  movies set lexemesSummary = to_tsvector(Summary);
update movies set rank = ts_rank(lexemesSummary, plainto_tsquery(
(
select Summary from movies where url='pirates-of-the-caribbean-the-curse-of-the-black-pearl'
)
));
drop table IF EXISTS recommendationsbasedonsummaryfield;
CREATE table recommendationsbasedonsummaryfield as select url,rank from movies where rank > -1 order by rank desc limit 50;
copy ( select * from recommendationsbasedonsummaryfield) to '/home/pi/RSL/top50reco_summaryPirate.csv' with csv;
