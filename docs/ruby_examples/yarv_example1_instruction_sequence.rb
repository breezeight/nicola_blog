require 'ripper'
require 'pp'

code = <<STR

def boh
end

class A ;
  def my_first_method(a,b)
    a + b
  end

  def my_second_method(b)
    my_first_method(1,a)
  end
end;

A.new.my_second_method(5)
STR

puts RubyVM::InstructionSequence.compile(code).disasm
