#ARGV[0]: margin error
#ARGV[1]: in_sample size
#ARGV[2]: out_of_sample size


### > input: ruby hoeffding_inequality.rb 0.05 735 20000
### > output: Hoeffding's inequality: 0.00607 < 0.05069881107691401 
### 모집단(개체수 20000)에서 735개의 sample을 뽑아 조사를 하였을 때, sample에서 조사된 확률이 실제 확률과 5% 이상 차이날 확률이 5.07%보다 낮다고 해석하면 된다!

$a = rand
$e = ARGV[0].to_f
$in_sample_size = ARGV[1].to_i
$out_of_sample_size = ARGV[2].to_i

def set_out_of_sample(size)
  positive = ($a * size).to_i
  negative = size - positive
  $out_of_sample = [1]*positive + [0]*negative
  $mu = ($out_of_sample.count(1).to_f)/size
end

def draw(size)
  in_sample = $out_of_sample.shuffle[0..(size-1)]
  $nu = (in_sample.count(1).to_f)/size
end

## Hoeffding inequality = P( |nu-mu| > e ) < 2*(e**(-2*in_sample_size*e**2))

set_out_of_sample($out_of_sample_size)

#each trial means an event of $in_sample_size draws out of $out_of_sample set
def trials(num)
  bad_events=0
  num.times do |trial|
    draw($in_sample_size)
    if ($mu - $nu).abs > $e
      bad_events += 1
    end
  end
  return bad_events.to_f/num
end

puts "a = " + $a.to_s #$a is the actual probability
puts "e = " + $e.to_s #$e is the margin error
rhs = 2*(2.718281828**(-2*$in_sample_size*$e**2)) #puts the RHS of the hoeffding inequality
lhs = trials(100000) #puts the left side of hoeffding inequality

puts "Hoeffding's inequlity: " + lhs.to_s + " < " + rhs.to_s