"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String


class StatefulMemoXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: define your own fields.
    memo_text = String(
        default="", scope=Scope.user_state,
        help="String of memo text",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the StatefulMemoXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/statefulmemo.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/statefulmemo.css"))
        frag.add_javascript(self.resource_string("static/js/src/statefulmemo.js"))
        frag.initialize_js('StatefulMemoXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def update_memo_text(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        self.memo_text = data['memo_text']
        self.runtime.publish(self, "write_memo", {"memo_text": self.memo_text})

        return {"memo_text": self.memo_text}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("StatefulMemoXBlock",
             """<statefulmemo/>
             """),
            ("Multiple StatefulMemoXBlock",
             """<vertical_demo>
                <statefulmemo/>
                <statefulmemo/>
                <statefulmemo/>
                </vertical_demo>
             """),
        ]
