.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes
  WHERE height > min AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE help AS
  SELECT child, height FROM parents, dogs WHERE name = parent ORDER BY height desc;
CREATE TABLE by_parent_height AS
  SELECT name FROM help, dogs WHERE name = child;


-- Sentences about siblings that are the same size
CREATE TABLE helper AS
  SELECT a.child AS one, b.child AS two FROM parents AS a, parents AS b WHERE a.parent = b.parent AND a.child < b.child;
CREATE TABLE sentences AS
  SELECT "The two siblings, " || one || " plus " || two || " have the same size: " || a.size FROM helper, size_of_dogs AS a, size_of_dogs AS b
    WHERE a.size = b.size AND a.name = one AND b.name = two;
