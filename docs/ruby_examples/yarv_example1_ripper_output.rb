require 'ripper'
require 'pp'

code = <<STR
class A < Array;
  def first
  end

  def second
  end
end;
STR

pp Ripper.sexp(code)
