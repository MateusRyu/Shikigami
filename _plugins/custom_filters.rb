module CustomFilters
  def remove_md_extension(input)
    input.gsub(/\.md\)/, ')')
  end
end

Liquid::Template.register_filter(Jekyll::LinkFilter)
