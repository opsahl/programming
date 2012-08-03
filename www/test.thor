class Test < Thor
    desc "example FILE", "an example task that does something with a file"
    def example(file)
        puts "You supplied the file: #{file}"
    end
end
