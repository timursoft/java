import styled from 'styled-components';

const Button = styled.button`
    background-color: ${({ theme }) => theme.colors.primary};
    color: ${({ theme }) => theme.colors.text};
    padding: ${({ theme }) => theme.spacing.medium};
    border: none;
    border-radius: 4px;
    cursor: pointer;

    &:hover {
        background-color: ${({ theme }) => theme.colors.secondary};
    }

    &:disabled {
        background-color: ${({ theme }) => theme.colors.background};
        color: ${({ theme }) => theme.colors.text};
        cursor: not-allowed;
    }
`;

export default Button;