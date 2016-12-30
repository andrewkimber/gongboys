# Perceptron learning algorithm을 이용한 learning process 연습.

# ARGV[0]: size of the learning set!
# ARGV[1]: size of the testing set!

# (0,1)*(0,1) 공간에서 random 점을 뽑아서, 그 점과 원점을 지나는 직선의 기울기를 $a로 설정 (결국 $a도 랜덤인 셈)
# hypothesis function 의 계수가 될 w를 initialize
# 목표는 learning process를 통해 실제 a에 가까운 w를 찾아가는 것.
random_x = rand
random_y = rand
$a = random_y / random_x
$w = 0.0

# 실제 정답에 해당하는 함수! f(x)
def answer_function(x)
  return $a*x
end

# hypothesis에 해당하는 함수. h(x)
def hypothesis_function(x)
  return $w*x
end

# sign 결정 함수
def sign(x)
  x>0 ? 1 : -1
end

# y-f(x)의 sign. 즉, output에 해당.
def answer_sign(elem)
  sign(elem[1]-answer_function(elem[0]))
end

# y-h(x)의 sign. hypothesis를 통해 예측하는 output.
def guess_sign(elem)
  sign(elem[1]-hypothesis_function(elem[0]))
end

# (0,1)*(0,1) 공간에서 random한 좌표를 argument 갯수만큼 뽑음.
random_set = []
ARGV[0].to_i.times do |time|
  x=rand
  y=rand
  random_set << [x,y]
end

# 현재 h(x)를 적용하였을 때, 제대로 된 output을 내지 못하는 점들을 뽑아냄.
def error_selection(set)
  error_set = []
  set.each do |elem|
    error_set << elem if (guess_sign(elem) != answer_sign(elem))
  end
  return error_set
end

# error_set 중에서 random하게 한 점을 골라, w = w + y*x를 적용시키는 learning algorithm.
# *** Perceptron learning algorithm (PLA) 참고!!***
def correction(error_set)
  sample_elem=error_set.sample
  $w = $w + guess_sign(sample_elem) * sample_elem[0]
end

trial=1

# error point가 없을 때까지 계속 루프!
while !error_selection(random_set).empty?
  error_set = error_selection(random_set)
  puts "trial: " + trial.to_s + ",  w :" + $w.to_s + ",   # of errors: " + error_set.count.to_s
  correction(error_set)
  trial+=1
end
puts "Finished after %{trial} trials!" % {:trial => trial}
puts "---------------------------------------"


puts "Number of learning samples: " + ARGV[0].to_s
puts "a = " + $a.to_s
puts "w = " + $w.to_s

puts "---------------------------------------"



puts "Now, let's test!"
# 이제 test를 해봅시다!




# test set을 만듭니다.
test_set = []
nums = ARGV[1].to_i

nums.times do |time|
  x=rand
  y=rand
  test_set.push [x,y]
end

# error가 몇개인지 찾아냅시다~
num_of_errors = error_selection(test_set).count

percentage = (num_of_errors.to_f / nums)*100
puts "Number of test samples: " + nums.to_s
puts "Accuracy: " + (100.0-percentage).to_s