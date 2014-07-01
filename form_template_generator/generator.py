__author__ = 'francois'


class Generator(object):

    def get_twitter_form(self, form):
        html = """<fieldset>
  <legend>FIELDSET LEGEND GOES HERE</legend>"""

        for field in form.visible_fields():
            field_html = TWITTER_FIELD_TEMPLATE\
                .replace("****FIELD_LABEL****", field.label)\
                .replace("****FIELD_NAME****", field.name)

            if field.field.required:
                field_html = field_html.replace("****FIELD_REQUIRED****", "required")
            else:
                field_html = field_html.replace("****FIELD_REQUIRED****", "")

            if field.help_text:
                field_html = field_html.replace("****FIELD_HELP_TEXT****", field.help_text)
            else:
                field_html = field_html.replace(
                    '<div class="col-sm-9 col-sm-offset-3 help-text">****FIELD_HELP_TEXT****</div>', ""
                )

            html += field_html

        html += """
</fieldset>"""

        return html


TWITTER_FIELD_TEMPLATE =  """
  <div class="form-group{% if form.****FIELD_NAME****.errors %} error{% endif %} ****FIELD_REQUIRED**** ">
    <label class="col-sm-3 control-label" for="id_****FIELD_NAME****">****FIELD_LABEL****</label>
    <div class="col-sm-7">
      {{ form.****FIELD_NAME**** }}
    </div>
    {% if form.****FIELD_NAME****.errors %}
      <div class="col-sm-9 col-sm-offset-3">{{ form.****FIELD_NAME****.errors }}</div>
    {% endif %}
    <div class="col-sm-9 col-sm-offset-3 help-text">****FIELD_HELP_TEXT****</div>
  </div>"""