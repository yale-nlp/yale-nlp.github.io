module Jekyll
    class GenerateProjects < Generator
      safe true
      priority :normal
  
      def generate(site)
        # Load 'projects' data file or assign an empty array if it doesn't exist
        projects = site.data["projects"]
  
        # Generate a page for each project
        projects.each do |project|
          site.pages << ProjectPage.new(site, project)
        end
      end
    end
  
    class ProjectPage < Page
      def initialize(site, project)
        @site = site
        @base = site.source
        @dir = File.join('projects', project['slug'])
        @name = 'index.html'
  
        self.process(@name)
        self.read_yaml(File.join(@base, '_layouts'), 'project_details.html')
        self.data = project
      end
    end
  end
  