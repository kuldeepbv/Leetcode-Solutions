select w2.id
from weather w1,weather w2
where w2.recorddate - w1.recorddate = 1 and w2.temperature > w1.temperature