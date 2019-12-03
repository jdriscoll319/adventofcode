#include <vector>
#include <iostream>

int process(std::vector<int> nums, int noun, int verb)
{
  nums[1] = noun;
  nums[2] = verb;

  size_t pos1, pos2, pos3;
  for (size_t i = 0; i != nums.size(); ++i)
  {
    switch (nums[i])
    {
      case 1:
        pos1 = nums[++i];
        pos2 = nums[++i];
        pos3 = nums[++i];
        nums[pos3] = nums[pos1] + nums[pos2];
        break;
      case 2:
        pos1 = nums[++i];
        pos2 = nums[++i];
        pos3 = nums[++i];
        nums[pos3] = nums[pos1] * nums[pos2];
        break;
      case 99:
        return nums[0];
      default:
        std::cout << nums[i];
        return 1;
    }
  }
}

int main()
{
  std::vector<int> nums {1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0};

  for (size_t noun = 0; noun <= 99; ++noun)
  {
    for (size_t verb = 0; verb <= 99; ++verb)
    {
      int res = process(nums, noun, verb);
      if ( res == 19690720)
      {
        std::cout << 100 * noun + verb << '\n';
        return 0;
      }
      if ( res == 1 )
      {
        std::cout << "\nYou dun fucked up\n";
        return 0;
      }
    }
  }

  return 0;
}
