class Heart
  def ok!
    puts "This method should not return errors"
    public_method
    protected_method
    private_method
  end

  def not_ok!
    puts "This method should raise errors"
    self.public_method    # OK
    self.protected_method # OK
    begin
      self.private_method   # raises NoMethodError
    rescue
      puts "Exception: #{$!}"
    end
  end

  def public_method; end

  protected
  def protected_method; end

  private
  def private_method; end
end

# Internal Visibility
Heart.new.ok!
Heart.new.not_ok!

# External Visibility
heart = Heart.new
heart.public_method    # => nil

begin
  heart.protected_method # => raises NoMethodError
rescue
  puts "Exception: #{$!}"
end

begin
  heart.private_method   # => raises NoMethodError
rescue
  puts "Exception: #{$!}"
end



#Exception: if the object sending the message is of the same type as the object receiving the message, then it’s OK to call protected methods.
class Hands < Heart
  def call_stuff r
    r.public_method    # => ok!
    r.protected_method # => ok, but only if self.is_a?(r.class)
    r.private_method   # => raises NoMethodError
  end
end


