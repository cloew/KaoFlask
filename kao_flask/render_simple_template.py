from flask import render_template

def render_simple_template(template):
  """ Returns a function that when called renders the given template """
  def run():
    return render_template(template)
  return run
