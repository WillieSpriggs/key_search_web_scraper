# data_compiler

Sprint 1: 
    * Develop Source, Website, Page, and Webpage classes.
    [class] Source: Foundation for the website class and other source types in the future.
        When initialized, creates an object of type source and creates itself an ID.
        Defines how to add and remove pages of a Source.
        Defines self destruction which allows the object to be garbage collected. (deletes all pages)
    [class] Website: [Extends Source] Defines the source type, and saves sites URL.
        When initialized, automatically generates page for site homepage.
    
    [class] Page: Foundation for Webpage class and other types of pages in the future.
        Requires a unique ID to be initialized. (Utomatically created when initialized
        from Website addPage function.) Page IDs are monitored by Website class.
        Generates a new file to hold key searched data. (The name of the file corresponds to the the Page ID)
        Defines for to read and write to key searched data file.
        Defines how Pages and corresponding files should be destroyed.
    [class] Webpage: [Extends Page] Saves webpage URL.
        Requires a unique ID to be initialize. 

    * Perform Google Search and return list of URLs
    * Create Website for each URL listed.

Sprint 2: 
    * Defensive coding and error prevention. [test and push]
    * Define how to scrape single webpage. (website homepage NO page crawling)
    * Write all  scraped contents to appropriate Webpage data file.
    * Scrape the homepages of multiple websites in one function call.
    * Destroy all website data when finished.

Spring 3:
    * Defensive coding and error prevention. [test and push]