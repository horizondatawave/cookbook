from textwrap import dedent
from crewai import Task

class MeetingPreparationTasks():
	def research_task(self, agent, participants, context):
		return Task(
			description=dedent(f"""\
				Your task is to conduct detailed research on all individuals and companies involved in the upcoming meeting.
            This includes gathering professional background, recent LinkedIn posts, and any other publicly available LinkedIn information.

            Steps to follow:
            1. Identify LinkedIn profiles for participants if they are not directly provided.
                - Use emails to infer names or company names.
                - Leverage domain names in email addresses to deduce the company name.
                - Try different variations of company names (e.g., "HorizonDataWave", "Horizon Data Wave", "HorizonDataWave.ai") during searches.
                - Utilize the `SearchLinkedInUsers` functionality for profile lookup using inferred or provided information.
                - Example: If the email is "a.brown@examplecompany.com", search with parameters like:
                    - "last_name: brown, company_keyword: example company"
                    - "last_name: brown, company_keyword: examplecompany"
                - Make several attempts with alternative spellings or formats to ensure the best chance of finding the correct profile.
            
            2. Collect information for each participant and their company:
                - Summarize their professional background.
                - Highlight any notable or recent LinkedIn posts.
                - Note relevant company details, including industry focus, recent news, or achievements.

            Context for your research:
            - Participants: {participants}
            - Meeting Context: {context}

            Ensure your research is thorough and presented in a structured, actionable format.
"""),
			expected_output=dedent("""\
				A detailed report summarizing key findings about each participant
				and company, highlighting information that could be relevant for the meeting."""),
			async_execution=True,
			agent=agent
		)

	def industry_analysis_task(self, agent, participants, context):
		return Task(
			description=dedent(f"""\
				Analyze the current industry trends, challenges, and opportunities
				relevant to the meeting's context. Consider market reports, recent
				developments, and expert opinions to provide a comprehensive
				overview of the industry landscape.

				Participants: {participants}
				Meeting Context: {context}"""),
			expected_output=dedent("""\
				An insightful analysis that identifies major trends, potential
				challenges, and strategic opportunities."""),
			async_execution=True,
			agent=agent
		)

	def meeting_strategy_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Develop strategic talking points, questions, and discussion angles
				for the meeting based on the research and industry analysis conducted

				Meeting Context: {context}
				Meeting Objective: {objective}"""),
			expected_output=dedent("""\
				Complete report with a list of key talking points, strategic questions
				to ask to help achieve the meetings objective during the meeting."""),
			agent=agent
		)

	def summary_and_briefing_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Compile all the research findings, industry analysis, and strategic
				talking points into a concise, comprehensive briefing document for
				the meeting.
				Ensure the briefing is easy to digest and equips the meeting
				participants with all necessary information and strategies.

				Meeting Context: {context}
				Meeting Objective: {objective}"""),
			expected_output=dedent("""\
				A well-structured briefing document that includes sections for
				participant bios, industry overview, talking points, and
				strategic recommendations."""),
			agent=agent
		)
