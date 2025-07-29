# ExerciseDB MCP Server

## Overview

The ExerciseDB MCP Server provides a comprehensive and structured API that features an extensive collection of over 1,300 exercises. Each exercise is meticulously categorized by body part, target muscle group, and the equipment required for the workout. The API is designed for seamless integration, making it an invaluable tool for developers building fitness applications, trainers creating personalized workout plans, and fitness enthusiasts seeking precise and actionable exercise guidance.

### Key Features

- **Extensive Exercise Library**: Access over 1,300 exercises complete with detailed metadata.
- **Categorization**: Exercises are organized by body part, target muscle group, and equipment needed.
- **Visual Aids**: High-quality form and follow-through animations are provided for each exercise, ensuring users can visualize the correct techniques.
- **Intuitive Interface**: The API is structured for easy and efficient access to exercise data.

## Tools and Endpoints

The ExerciseDB MCP Server offers various endpoints and functionalities, allowing for targeted data retrieval:

1. **Exercises by Body Part**
   - Endpoint: `/exercises/bodyPart/{bodyPart}`
   - Description: Returns a list of exercises based on the specified body part.

2. **List of Body Parts**
   - Endpoint: `/exercises/bodyPartList`
   - Description: Retrieves a list of all available body parts.

3. **List of Equipment**
   - Endpoint: `/exercises/equipmentList`
   - Description: Retrieves a list of all available equipment.

4. **List of Target Muscles**
   - Endpoint: `/exercises/targetList`
   - Description: Retrieves a list of all target muscles.

5. **Exercises by Equipment**
   - Endpoint: `/exercises/equipment/{type}`
   - Description: Returns a list of exercises based on specified equipment type.

6. **Exercises by Target Muscle**
   - Endpoint: `/exercises/target/{target}`
   - Description: Returns a list of exercises targeting a specific muscle.

7. **Exercise by ID**
   - Endpoint: `/exercises/exercise/{id}`
   - Description: Returns details of an exercise by its unique ID.

8. **Exercises by Name**
   - Endpoint: `/exercises/name/{name}`
   - Description: Returns a list of exercises matching a specific name.

9. **All Exercises**
   - Endpoint: `/exercises`
   - Description: Returns a list of all available exercises.

## Notes

- **List Pagination**: By default, list endpoints return 10 items to enhance data transfer speed. Use the `limit` and `offset` query parameters to paginate results according to your needs.
  
- **Dynamic Image URLs**: The property `gifUrl` on each exercise changes daily at 12:00pm US Central Time. Ensure that your application can handle expired URLs appropriately to avoid image outages.

## Terms of Use

1. **Ownership**: All data and content are the property of ExerciseDB MCP Server.
2. **Usage Rights**: Licensed use is granted as per subscription terms, and is non-transferable.
3. **Termination**: Rights are revoked upon subscription termination, requiring cessation of use and data deletion.
4. **Caching Prohibition**: Data must be freshly requested for each use; caching is prohibited.
5. **Prohibited Uses**: Redistribution, reselling, and sublicensing of data are prohibited.
6. **Changes to Terms**: Terms of Use may be modified; continued use implies acceptance.

For further details or inquiries, please contact the support team.