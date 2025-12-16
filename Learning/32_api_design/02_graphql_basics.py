GRAPHQL_SCHEMA = '''
type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]
}

type Post {
    id: ID!
    title: String!
    content: String!
    author: User!
}

type Query {
    users: [User!]
    user(id: ID!): User
    posts: [Post!]
}

type Mutation {
    createUser(name: String!, email: String!): User!
    createPost(title: String!, content: String!, authorId: ID!): Post!
}
'''

RESOLVERS = '''
Query: {
    users: () => db.users,
    user: (_, { id }) => db.users.find(u => u.id === id),
    posts: () => db.posts,
}
Mutation: {
    createUser: (_, { name, email }) => {
        const user = { id: Date.now(), name, email };
        db.users.push(user);
        return user;
    }
}
'''

print('GraphQL schema defined!')
