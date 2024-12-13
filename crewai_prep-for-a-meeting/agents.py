from textwrap import dedent
from crewai import Agent
from hdw_tools.tools import crewai_linkedin
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool


class MeetingPreparationAgents():
	def research_agent(self):
		return Agent(
			role='Research Specialist',
			goal='Conduct thorough research on people and companies involved in the meeting in LinkedIn',
			tools=[
				crewai_linkedin.GetLinkedInCompany(),
				crewai_linkedin.GetLinkedInCompanyPosts(),
				crewai_linkedin.GetLinkedInGroup(),
				crewai_linkedin.GetLinkedInPost(),
				crewai_linkedin.GetLinkedInPostComments(),
				crewai_linkedin.GetLinkedInPostReactions(),
				crewai_linkedin.SearchLinkedInCompanies(),
				crewai_linkedin.SearchLinkedInEducations(),
				crewai_linkedin.SearchLinkedinIndustries(),
				crewai_linkedin.SearchLinkedInLocations(),
				crewai_linkedin.SearchLinkedInUsers(),
				crewai_linkedin.GetLinkedInUser(),
				crewai_linkedin.GetLinkedInUserPosts(),
				crewai_linkedin.SearchLinkedinJobs()
				   ],
			backstory=dedent("""\
					As a Research Specialist, your mission is to uncover detailed information
					about the individuals and entities participating in the meeting. Your insights
					will lay the groundwork for strategic meeting preparation."""),
			verbose=True
		)

	def industry_analysis_agent(self):
		return Agent(
			role='Industry Analyst',
			goal='Analyze the current industry trends, challenges, and opportunities',
			tools=[ScrapeWebsiteTool(), SerperDevTool()],
			backstory=dedent("""\
					As an Industry Analyst, your analysis will identify key trends,
					challenges facing the industry, and potential opportunities that
					could be leveraged during the meeting for strategic advantage."""),
			verbose=True
		)

	def meeting_strategy_agent(self):
		return Agent(
			role='Meeting Strategy Advisor',
			goal='Develop talking points, questions, and strategic angles for the meeting',
			tools=[ScrapeWebsiteTool(), SerperDevTool()],
			backstory=dedent("""\
					As a Strategy Advisor, your expertise will guide the development of
					talking points, insightful questions, and strategic angles
					to ensure the meeting's objectives are achieved."""),
			verbose=True
		)

	def summary_and_briefing_agent(self):
		return Agent(
			role='Briefing Coordinator',
			goal='Compile all gathered information into a concise, informative briefing document',
			tools=[ScrapeWebsiteTool(), SerperDevTool()],
			backstory=dedent("""\
					As the Briefing Coordinator, your role is to consolidate the research,
					analysis, and strategic insights."""),
			verbose=True
		)
