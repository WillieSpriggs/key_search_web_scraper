# data_compiler

Sprint 1: 
    * Develop Source, Website, Page, and Webpage classes.
    [class] Source: Foundation for the website class and other source types in the future.
        When initialized, creates an object of type source.
        Defines how to add and remove pages of a Source.
        Defines self destruction which allows the object to be garbage collected. (deletes all pages)
    [class] Website: [Extends Source] Defines the source type, and saves sites URL.
        When initialized, automatically generates page for site homepage.
    
    [class] Page: Foundation for Webpage class and other types of pages in the future.
        Requires a unique ID to be initialized. (Atomatically created when initialized
        from Website addPage function.) Page IDs are monitored by Website class.
        Generates a new file to hold key searched data once pushToDataFile function has been envoked. 
        (The name of the file corresponds to the the Page ID)
        Defines functions to read and write to key searched data file.
        Defines how Pages and corresponding files should be destroyed.
    [class] Webpage: [Extends Page] Saves webpage URL.
        Requires a unique ID to be initialize. 

    * Perform Google Search and return list of URLs
    * Create Website for each URL listed.

Sprint 2: 
    * Defensive coding and error prevention. [test and push]
    * Define how to scrape single webpage. (website homepage NO page crawling)
    * Write all scraped contents to appropriate Webpage data file.
        Define constructPages (Source) and parseWebpage (Webpage) functions.
    * Scrape the homepages of multiple websites in one function call.
    * Destroy all websites data when finished.

Spring 3:
    * Defensive coding and error prevention. [test and push]
    * Add key word feature.
    * Parse paragraph tag based on given keys and push contents to data file.
    * Format page data files for reading using html tags.

Sprint 4:
    * Defensive coding and error prevention. [test and push]
    * Read google query, number of search results, keywords, and number of supporting sentences from command line.
    * If needed, pull key sentences from previous paragraph tag.
        In the case of short paragraphs, supporting sentences may span across multiple paragraph tags.
        Test url: https://www.biography.com/us-president/barack-obama
    * Create JSON file with names of websites and corresponding pages.

Sprint 5:
    * Defensive coding and error prevention. [test and push]
    * Research web crawlers and efficient web crawing methods.
    * Create web crewling method for Website class.
    * Within the website constructor, call web crawler method and add Webage for each new page.
    * Successfully keysearch all pages of a website.

Sprint :
    * Read data from appropriate page and print it to screen.
        Define readFromPage function given page reference and data.
    * Read all data from multiple websites using single function call.
    
Stretch Goals:
    * Determine if string is safe to be pushed to file (doesn't contain weird characters).
        The Wikipedia error [https://en.wikipedia.org/wiki/Dobermann]
            Background: When the program tries to write unknown characrters to file, parseWebpage function breaks.
            Writes to file until it reaches unknown character.
            Possible solutions: Before calling push to file, check if the paragraph contains only basic characters.
            If the program fails to write to file, skip that iteration and keep moving forward.