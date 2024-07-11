module CustomFilters
  def erase_md_extension(input)
    input.gsub(/\.md\)/, ')')
  end
end

Liquid::Template.register_filter(CustomFilters)
