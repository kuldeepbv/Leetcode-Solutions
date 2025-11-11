select w1.id
from weather w1
join weather w2 on w2.recorddate = w1.recorddate - 1 and w1.temperature > w2.temperature