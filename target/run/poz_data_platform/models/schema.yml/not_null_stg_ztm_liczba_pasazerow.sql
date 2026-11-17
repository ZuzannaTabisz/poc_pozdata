
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select liczba_pasazerow
from "poz_data"."main"."stg_ztm"
where liczba_pasazerow is null



  
  
      
    ) dbt_internal_test