show databases;
use journaux;
show tables;
drop table articles;

select * from articles;
create database journaux;

create table articles(
id_article int primary key not null auto_increment,
titre varchar(250) not null,
jour_publication DATE,
categorie varchar(100),
journal varchar(15)
)
    ENGINE = InnoDB;
    
select journal, max(jour_publication) as max, min(jour_publication) as min
from articles
group by journal;

Select jour_publication, journal, count(*) from articles  where jour_publication<=date('2021-05-10') and  jour_publication>=date('2020-9-10')
group by jour_publication, journal;

select * from articles where journal='Le Monde'and where jour_publication<=date('2021-05-10') and jour_publication>=date('2020-9-10');